from django.shortcuts import render,redirect,get_object_or_404
from .models import Toppicks, Register, Trind,Mobile
from .forms import LoginForm,RegisterForm

from .utils.search import apply_search 

def home(request):
    return render(request, 'home.html')




# ---------------- PRODUCT DETAIL ----------------
def product_detail(request):
    electronics = Toppicks.objects.all()

    electronics = apply_search(
        electronics,
        request,
        fields=['brand', 'model_name']
    )

    return render(request, 'product_detail.html', {
        'electronics': electronics
    })


# ---------------- TREND VIEW ----------------
def trind_view(request):
    test = Trind.objects.all()

    test = apply_search(
        test,
        request,
        fields=['name', 'model_name']
    )

    return render(request, "latest.html", {
        'test': test
    })


# ---------------- MOBILE VIEW ----------------
def mobile_croma(request):
    mobile = Mobile.objects.all()

    mobile = apply_search(
        mobile,
        request,
        fields=['name', 'model_name']
    )

    return render(request, "mobile_croma.html", {
        'mobile': mobile
    })

def global_search(request):
    q = request.GET.get('q')

    products = Toppicks.objects.all()
    mobiles = Mobile.objects.all()
    trends = Trind.objects.all()

    if q:
        products = apply_search(products, request, ['brand', 'model_name'])
        mobiles = apply_search(mobiles, request, ['name', 'model_name'])
        trends = apply_search(trends, request, ['name', 'model_name'])

    return render(request, 'search.html', {
        'products': products,
        'mobiles': mobiles,
        'trends': trends,
        'query': q
    })





# -----------register---------------

def register(request):
    mgs = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        email = request.POST.get("email")

        if Register.objects.filter(email = email).exists():
            mgs = "email already exist"
         
        else:
         if form.is_valid():
             form.save()
             return redirect("login")        
    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form, "mgs":mgs})




# ----------------------login--------------
def login(request):
    mgs = ""
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = Register.objects.get(username=username, password=password)

            request.session["username"] = user.username
            response = redirect('home')
            response.set_cookie("username", user.username)
            return response

        except Register.DoesNotExist:
            mgs = "invalid username or password"

    return render(request, 'login.html', {'form': form, 'mgs': mgs})



def logout(request):
    request.session.flush()
    return redirect("login")




# ---------------details pages------

def product_list(request, id):
    i = get_object_or_404(Toppicks, id=id)
    return render(request, 'product_list.html', {'i': i})


def latest_list(request, id):
    b = get_object_or_404(Trind, id=id)
    return render(request, 'latest_list.html', {'b': b})



def mobile_list(request, id):
    m = get_object_or_404(Mobile, id=id)
    return render(request, 'mobile_list.html', {'m': m})



# --------------------cart system----------------------

def add_to_cart(request, id):

    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart

    return redirect(request.META.get("HTTP_REFERER"))



def cart_view(request):

    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for id, quantity in cart.items():
        product = Toppicks.objects.get(id=id)
        
        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })




def remove_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart

    return redirect('cart')


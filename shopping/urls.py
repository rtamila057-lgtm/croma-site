from django.contrib import admin
from django.urls import path
from . import views  

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
    path('register/', views.register, name='register'),
    path('latest/', views.trind_view, name='latest'),
    path('product/', views.product_detail, name='product'),
    path('mobile/', views.mobile_croma, name='mobile'),
    path('latest_list/<int:id>/', views.latest_list, name='latest_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product_list/<int:id>/', views.product_list, name='product_list'),
    path('mobile_list/<int:id>/', views.mobile_list, name='mobile_list'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-cart/<int:id>/', views.remove_cart, name='remove_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('search/', views.global_search, name='search')




    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
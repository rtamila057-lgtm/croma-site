from django.db import models

# Create your models here.


class Toppicks(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productimage/')



class Register(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
       return self.username 
    


class Trind(models.Model):

    name = models.CharField(max_length=150)

    model_name = models.CharField(max_length=150)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='trind/')

    def __str__(self):
        return self.name


class Mobile(models.Model):

    name = models.CharField(max_length=150)

    model_name = models.CharField(max_length=150)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    storage = models.CharField(max_length=50, blank=True, null=True)

    # battery = models.CharField(max_length=50, blank=True, null=True)

    image = models.ImageField(upload_to='productimage/')


    def __str__(self):
        return self.name


   
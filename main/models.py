from django.db import models
from django .contrib.auth.models import User
from django_countries.fields import CountryField
from django.conf import settings
from django.shortcuts import reverse
from django.utils.timezone import now

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    custamer_id = models.CharField(max_length=50,blank=True)
    buyings = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class Cat(models.Model):
    cat = models.CharField(max_length=100)
    def __str__(self):
        return self.cat

class Types(models.Model):
    image = models.ImageField(upload_to = 'static/')
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    size = models.CharField(max_length=4)
    location = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    availabilty = models.BooleanField()
    gender = models.BooleanField()
    date = models.DateField()
    cat = models.ForeignKey(Cat, on_delete = models.CASCADE)   

    def __str__(self):
        return self.title
    
    def add_to_cart_url(self):
        return reverse('add_to_cart',kwargs = {'slug':self.slug})

    def remove_from_cart_url(self):
        return reverse('remove_from_cart',kwargs = {'slug':self.slug})

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    orderd = models.BooleanField(default=False)
    types = models.ForeignKey(Types,on_delete = models.CASCADE)
    quanty = models.IntegerField(default=1)
    
    def pricecart(self):
        return self.types.price * self.quanty

    

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    charge_id = models.CharField(max_length=50)
    amount = models.FloatField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    orderd = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    startdate = models.DateField(default= now)
    address =  models.TextField(null= True)
    country = CountryField(multiple = False)
    recived = models.BooleanField(default=False)
    refund = models.BooleanField(default=False)
    payment = models.ForeignKey (Payment,on_delete=models.SET_NULL,null=True,blank=True)

    def total(self):
        total = 0
        for i in self.items.all():
            total = total + i.pricecart()
        return total

















from django.contrib import admin
from .models import Order,Payment,OrderItem,Cat,Types,Userprofile


# Register your models here.
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(OrderItem)
admin.site.register(Cat)
admin.site.register(Types)
admin.site.register(Userprofile)


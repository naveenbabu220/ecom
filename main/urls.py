from django.urls import path
from.import views

urlpatterns = [
    path('',views.home ,name = 'home' ),
    path('cat/',views.cat, name = 'cat'),
    path('cat/<str:idd>/',views.types,name = 'type'),
    path('payment/',views.payment,name='payment'),
    path('add_to_cart/<slug>',views.add_to_cart,name = 'add_to_cart'),
    path('remove_from_cart/<slug>',views.remove_from_cart, name = 'remove_from_cart'),
    path('summary/',views.summary,name = 'summary'),
    path('address/',views.address,name = 'address'),
    
    
]
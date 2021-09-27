from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = "index_url"),
    path('/about', views.about,name = "about_url"),
    path('/cart', views.cart,name = "cart_url"),
    path('/contactus', views.contactus,name = "contactus_url"),
    path('/chicken', views.chicken,name = "chicken_url"),
    path('/desserts', views.desserts,name = "desserts_url"),
    path('/mutton', views.mutton,name = "mutton_url"),
    path('/nonvegsoup', views.nonvegsoup,name = "nonvegsoup_url"),
    path('/nonvegstarte/', views.nonvegstarter,name = "nonvegstarter_url"),
    path('/order', views.order,name = "order_url"),
    path('/payment', views.payment,name = "payment_url"),
    path('/rice', views.rice,name = "rice_url"),
    path('/roti', views.roti,name = "roti_url"),
    path('/seafood', views.seafood,name = "seafood_url"),
    path('/vegetariandishes', views.vegetariandishes,name = "vegetariandishes_url"),
    path('/starter', views.starter,name = "starter_url"),
    path('/vegsoups', views.vegsoups,name = "vegsoups_url"),
    
]

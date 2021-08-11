from django.urls import path
from .views import authenticate, contact_us_backend, home, login, order, order_confirmation, order_payment, payment_success, register, reservation_backend, user

urlpatterns = [
    path('', home, name="home"),
    path('u/<str:pk>', user, name="user"),
    path('order/', order, name="order"),
    path('confirm-order/<int:pk>/', order_confirmation, name="order_confirmation"),
    path('payment/<int:pk>/', order_payment, name="order_payment"),
    path('payment/success/<int:pk>/', payment_success, name="payment_success"),
    path('contact-us/',contact_us_backend,name='contact_us'),

    path('authenticate/', authenticate, name="authenticate"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('reservation-backend/', reservation_backend, name="reservation_backend")
]
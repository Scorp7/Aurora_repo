from django.urls import path
from .views import add_show, delete_data, edit_data, test_data

urlpatterns = [
    path('test/', test_data, name="test_data"),
    path('',add_show, name="add_show"),
    path('delete/<int:id>/', delete_data, name="delete_data"),
    path('<int:id>/', edit_data, name="edit_data"),
    
]

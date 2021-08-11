from administration.views import admin_change_order_status, admin_create_menu, admin_create_table, admin_create_todays_special, admin_create_user, admin_delete_contact_us, admin_delete_menu, admin_delete_order, admin_delete_reservation, admin_delete_table, admin_delete_todays_special, admin_delete_user, admin_detail_order, admin_detail_reservation, admin_edit_menu, admin_edit_order, admin_edit_reservation, admin_edit_table, admin_edit_todays_special, admin_edit_user, admin_home, admin_list_contact_us, admin_list_menu, admin_list_order, admin_list_reservation, admin_list_table, admin_list_todays_special, admin_list_user, admin_toggle_todays_special
from django.urls import path

urlpatterns = [
    path('', admin_home, name="admin_home"),
    path('all-users/', admin_list_user , name="admin_list_user" ),
    path('create-user/', admin_create_user, name="admin_create_user"),
    path('edit-user/<int:pk>/', admin_edit_user, name="admin_edit_user"),
    path('delete-user/<int:pk>/', admin_delete_user, name="admin_delete_user"),

    #Menu
    path('menu/', admin_list_menu, name="admin_list_menu"),
    path('create-menu-item/', admin_create_menu, name="admin_create_menu"),
    path('edit-menu-item/<int:pk>', admin_edit_menu, name="admin_edit_menu"),
    path('delete-menu-item/<int:pk>', admin_delete_menu, name="admin_delete_menu"),

    #Todays Special
    path('todays-special/', admin_list_todays_special, name="admin_list_todays_special"),
    path('create-todays-special/', admin_create_todays_special, name="admin_create_todays_special"),
    path('edit-todays-special/<int:pk>/', admin_edit_todays_special, name="admin_edit_todays_special"),
    path('delete-todays-special/<int:pk>/', admin_delete_todays_special, name="admin_delete_todays_special"),
    path('toggle-todays-special/<int:pk>/', admin_toggle_todays_special, name="admin_toggle_todays_special"),

    #Tables
    path('tables/', admin_list_table, name="admin_list_table"),
    path('create-table/', admin_create_table, name="admin_create_table"),
    path('edit-table/<int:pk>', admin_edit_table, name="admin_edit_table"),
    path('delete-table/<int:pk>', admin_delete_table, name="admin_delete_table"),

    #reservation
    path('reservations/',admin_list_reservation,name="admin_list_reservation"),
    path('edit-reservation/<int:pk>',admin_edit_reservation,name="admin_edit_reservation"),
    path('delete-reservation/<int:pk>',admin_delete_reservation,name="admin_delete_reservation"),
    path('detail-reservation/<int:pk>',admin_detail_reservation,name="admin_detail_reservation"),
    

    #order
    path('orders/', admin_list_order, name="admin_list_order"),
    path('edit-order/<int:pk>', admin_edit_order, name="admin_edit_order"),
    path('delete-order/<int:pk>', admin_delete_order, name="admin_delete_order"),
    path('detail-order/<int:pk>', admin_detail_order, name="admin_detail_order"),
    path('change-order-status/<int:pk>', admin_change_order_status, name="admin_change_order_status"),


    path('contact-us/', admin_list_contact_us,name="admin_list_contact_us"),
    path('delete-contact-us/<int:pk>', admin_delete_contact_us,name="admin_delete_contact_us")






]

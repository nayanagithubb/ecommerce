from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('add_category',views.add_category,name="add_category"),
    path('add_categorydb/<int:cat_id>',views.add_categorydb,name="add_categorydb"),
    path('show_category',views.show_category,name="show_category"),
    path('add_product',views.add_product,name="add_product"),
    path('add_productdb',views.add_productdb,name="add_productdb"),
    path('show_product',views.show_product,name="show_product"),
    path('delete_page/<int:pk>',views.delete_page,name="delete_page"),
    path('signuppage',views.signuppage,name="signuppage"),
    path('add_userdb',views.add_userdb,name="add_userdb"),
    path('user_home',views.user_home,name="user_home"),
    path('show_user',views.show_user,name="show_user"),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('add_to_cart/<int:pk>',views.add_to_cart,name="add_to_cart"),
    path('cart',views.cart,name="cart"),
    path('delete_cart/<int:pk>',views.delete_cart,name="delete_cart")
  

]


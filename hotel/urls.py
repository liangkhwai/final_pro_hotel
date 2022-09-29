from urllib.parse import urlparse
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('addrooms',views.addrooms,name='addrooms'),
    path('addtype',views.addtype,name='addtype'),
    path('editcustomer/<int:pk>',views.editcustomer,name='editcustomer'),
    path('editpassword/<int:pk>',views.editpassword,name='editpassword'),
    path('editrooms/<int:pk>',views.editrooms,name='editrooms'),
    path('edittype/<int:pk>',views.edittype,name='edittype'),
    path('fetchrooms',views.fetchrooms,name='fetchrooms'),
    path('roomdetail/<int:pk>',views.roomdetail,name='roomdetail'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
]

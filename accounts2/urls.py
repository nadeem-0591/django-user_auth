from django.urls import path
from .views import home,register,login_user,logout_user

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),

    


]
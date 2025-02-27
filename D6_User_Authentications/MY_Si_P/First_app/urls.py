from django.contrib import admin
from django.urls import path
from First_app import views
app_name='relative'
urlpatterns = [
    path('',views.index,name='index'),
    path('reg/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('userlogin/',views.user_login,name='u_log'),
    path('logout/',views.usr_logout,name='logout'),
            

]
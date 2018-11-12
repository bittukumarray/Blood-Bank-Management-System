from django.urls import path,re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.SignUp, name="signup"),
    path('login/', views.LogIn, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('about/', views.about, name="about"),
]

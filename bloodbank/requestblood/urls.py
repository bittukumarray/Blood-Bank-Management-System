from django.urls import path
from . import views

app_name = 'requestblood'

urlpatterns = [
    path('', views.index, name='index'),
    path('sorry/', views.sorry, name='sorry'),
    path('response/', views.response, name='response'),
]

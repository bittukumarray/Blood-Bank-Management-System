from django.urls import path
from . import views

app_name = "pathlab"

urlpatterns = [
    path('', views.index),
    path('result', views.result, name = "result")
]

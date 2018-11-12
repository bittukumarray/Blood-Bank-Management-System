from django.urls import path
from . import views

app_name = "pathlab"

urlpatterns = [
    path('hello/', views.hello),
]

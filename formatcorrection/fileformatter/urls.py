from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.mainpage, name = "main page"),
    path('displayfile/', views.displayfile, name = "main page")
]
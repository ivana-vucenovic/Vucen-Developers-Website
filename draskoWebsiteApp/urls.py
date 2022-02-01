from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('contact', views.contact),

]

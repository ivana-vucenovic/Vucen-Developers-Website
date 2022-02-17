from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    # path('about', views.about),
    # path('services', views.services),
    path('contact', views.contact),
    path('contactUs', views.contactUs),
    path('privacy', views.privacy),
    path('contactMessage', views.create),
]

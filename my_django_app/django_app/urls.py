
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_app  , name='django_app' )
]

# Handles the urls on the app side
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
]

# Handles the urls on the app side
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('logout', views.logout),
    path('login', views.login),
    # Actual path need to build out with a database
    #path('login/<int:user_id>', views.login),
]

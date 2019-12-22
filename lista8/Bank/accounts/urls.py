# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('logout_view/', views.SignUp, name='logout')
]
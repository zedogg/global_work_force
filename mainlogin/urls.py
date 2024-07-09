from . import views
from django.urls import path

urlpatterns = [
    path('',views.login),
    path('register',views.register),
    path('logout',views.logout),
  
   
]
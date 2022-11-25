from django.urls import path
from . import views

# Create your urlpatterns here

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
]
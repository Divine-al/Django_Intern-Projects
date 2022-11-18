from django.urls import path
from . import views

# Create your urlpatterns here

urlpatterns = [
    path('', views.index, name='index'),
    path('costumer_bookings', views.costumer_bookings, name='costumer_bookings'),
    path('costumer_order', views.costumer_order, name='costumer_order'),
]
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def costumer_order(request):
    return render(request, 'costumer_order.html')

def costumer_bookings(request):
    return render(request, 'costumer_bookings.html')
    
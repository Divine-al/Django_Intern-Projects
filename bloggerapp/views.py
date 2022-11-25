from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth 
from django.contrib import messages

# Create your views here.-

def index(request):
    return render(request, 'register.html')
    
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'usename already exits')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exits')
                return redirect('register')
            else:
               user =  User.objects.create_user(username=username, email=email, password=password)
               user.save()
               return redirect('login')

        else:
            messages.info(request, 'password is not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

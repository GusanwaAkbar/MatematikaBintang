
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()

from django. db import IntegrityError

#from django.contrib.auth import login as auth_login


# Create your views here ;

def home (request):
    return render(request,'index.html')

def beta (request):
    return render(request,'blogpost3.html')

def logout (request):
    logout(request)

    

def index (request):

    user = request.user

    context = {
        user : user
    }

    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST['email']
        password = request.POST['password1']
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                "output" : 'Welcome back,' + username,
            }
            return redirect('/beta',context)
        else:
            context = {
                "output" : "email atau password salah, silahkan login ulang"
            }
            return render(request, 'index.html', context)

    #SIGN_UP
    elif request.method == 'POST' and 'register' in request.POST:
        try:
            email = request.POST['email']
            password = request.POST['password1']
            saveuser = User.objects.create_user(email= email, password=password)
            
            context = {
                "output" : "register berhasil, silahkan login"
            }

            return render(request,'index.html',context)

        except IntegrityError:

            context = {
                "output" : "register gagal, email sudah terdaftar"
            }     

            return render(request,'index.html',context) 
    
    return render(request,'index.html',context)
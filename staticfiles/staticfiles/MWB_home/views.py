
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
    return render(request,'beta.html')

def index (request):
    if request.method == 'POST' and 'btn_login' in request.POST:
        username = request.POST['email']
        password = request.POST['password1']
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form})

    #SIGN_UP
    elif request.method == 'POST' and 'btn_signup' in request.POST:
        try:
            email = request.POST['email']
            password = request.POST['password1']
            saveuser = User.objects.create_user(email= email, password=password)
        except IntegrityError:
            return render(request,'index.html') 
    
    return render(request,'index.html')
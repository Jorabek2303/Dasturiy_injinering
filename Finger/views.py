from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def HomeView(request):

    return render(request,'home.html')


def LoginView(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('malumot')
        
    return render(request,'login.html')

@login_required(login_url="/register/")
def LogoutView(request):
    logout(request)
    return render(request,'home.html')


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
        
    return render(request, 'register.html', {'form': form})

@login_required(login_url="/register/")
def ProfileView(request, pk):
    profile = ProfileModel.object.all()

    return render(request, 'home.html', {'profile': profile, 'pk': pk})
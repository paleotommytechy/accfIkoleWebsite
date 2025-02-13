from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Announcement


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        #Validate passwords
        if password1 != password2:
            messages.error(request,'Passwords do not match')
            return redirect('register')
        
        #Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')
        
        #Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('register')
        
        #Create and save user
        user = User.objects.create_user(username=username,email=email, password=password1)
        user.save()

        messages.success(request, 'Registration Successful! You can now log in.')
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Login Successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'You have been logged out.')
    return redirect('login')
@login_required(login_url='/login/')
def dashboard(request):
    announcements = Announcement.objects.order_by('-date_posted')
    return render(request, 'dashboard.html',{'announcements':announcements})
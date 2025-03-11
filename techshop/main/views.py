from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser



def index(request):
    return render(request,'index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
   
    
    return render(request,'login.html')


def signup_user(request):
    if request.method == "POST":
        name = request.POST.get('')
        username = request.POST.get('username')
        password = request.POST.get('password')
        conf_password = request.POST.get('confirm-password')
        if password == conf_password:
            user = CustomUser.objects.create_user(username=username,password=password , is_student=True)
            user.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
        
        else:
            messages.error(request, "Passwords do not match!")

    return render(request,'signup.html')

def user_logout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .models import student

# Home page view
def home(request):
    return render(request, "home.html")

# About page view
def about(request): 
    return render(request, "about.html")

# Contact page view
def contact(request):
    s = student.objects.all()
    return render(request, "contact.html", {'student_list': s})

# Student details
def details(request, slug):  
    student_obj = get_object_or_404(student, slug=slug)  
    return render(request, "details.html", {'student': student_obj})

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# ✅ Login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('contact')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})  # ✅ Correct dictionary format

# ✅ Logout view
def logout(request):
    if request.method == 'POST':
        auth_logout(request)  # ✅ avoid recursion
        return redirect('home')
    return render(request, 'logout.html')

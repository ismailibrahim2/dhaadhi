from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from courses.models import Category, Course, Requirements, Benifits, Module, Lesson
from .forms import UserRegistrationForm


def register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, 'Registration successful.')
            return redirect('students:homepage')
        messages.error(
            request, "Unsucessful registration, Invalid information")
    form = UserRegistrationForm()
    return render(request, 'students/auth/registration.html', context={'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request, "students:homepage")
            else:
                return messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username and Password")
            # return redirect(request, 'students:login')
    form = AuthenticationForm()
    return render(request, template_name="students/auth/login.html", context={'form': form})


def home(request):
    return render(request, 'index.html')

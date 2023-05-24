from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from users.models import CoachProfile, CustomerProfile
from django.contrib.auth.forms import UserCreationForm
from .models import User

from users.models import Customer, Coach
from .forms import SignUpForm
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug statement
            role = form.cleaned_data['role']
            print("Selected role:", role)  # Debug statement
            if role == 'CUSTOMER':
                user = Customer.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'],
                    role=role
                )
                print("Customer user created:", user.username)  # Debug statement
            elif role == 'COACH':
                user = Coach.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'],
                    role=role
                )
                print("Coach user created:", user.username)  # Debug statement
            else:
                print("Invalid role")  # Debug statement
                # Handle other roles or error cases as per your requirements
                pass
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            print("Form is not valid")  # Debug statement
            print(form.errors)  # Debug statement
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


# from django.contrib import messages




from django.contrib import messages, admin
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        print(f"username: {username}, password: {password}, role: {role}")

        user = authenticate(request, username=username, password=password)
        print(f"authenticated user: {user}")

        if user is not None:
            if user.role == role:
                login(request, user)
                if role == 'ADMIN':
                    return redirect('/admin/')  # Redirect to the Django admin panel
                else:
                    return HttpResponse(f"WELCOME {role.upper()}!")
            else:
                messages.error(request, 'Invalid role')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')


# def logout_view(request):
#     logout(request)
#     return redirect('login')


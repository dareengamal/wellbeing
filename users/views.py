from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import User ,CoachProfile, CustomerProfile

from users.models import Customer, Coach
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug statement
            role = form.cleaned_data['role']
            print("Selected role:", role)  # Debug statement
            if role == 'CUSTOMER':
                user = User.objects.create(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'],
                    role=role
                )
                print("Customer user created:", user.username)  # Debug statement
            elif role == 'COACH':
                user = User.objects.create(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'],
                    role=role
                )
                print("Coach user created:", user.username)  # Debug statement
            else:
                print("Invalid role")  # Debug statement
                
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

        user = authenticate(request=request, username=username, password=password)
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

# views.py

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect
from .utils import send_password_reset_email

def forget_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.get(email=email)

        # Generate the reset link
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        current_site = get_current_site(request)
        reset_link = f"http://{current_site.domain}/reset/{uid}/{token}/"

        # Send the password reset email
        send_password_reset_email(user, reset_link)

        # Render a success message or redirect to a success page
        return redirect('password_reset_done')
    else:
        return render(request, 'forget_password.html')

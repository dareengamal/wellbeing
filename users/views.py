from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login

from users.models import CoachProfile, CustomerProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to appropriate view based on user role
            if user.role == 'CUSTOMER':
                # return redirect('customer_home')
                return HttpResponse("WELCOME!")
            elif user.role == 'COACH':
               return HttpResponse("WELCOME!")
            elif user.role == 'ADMIN':
               return HttpResponse("WELCOME!")
        else:
            # Authentication failed, handle error
            return HttpResponse('Invalid credentials')
    else:
        # Render login form
        return render(request, 'login.html')




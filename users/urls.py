
from django.urls import path
from users import views
from .views import register
from django.contrib.auth import views as auth_views
from .views import forget_password

urlpatterns = [
    path('login/', views.login_view, name='login'),
    #  path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name='register'),



    path('forget-password/', forget_password, name='forget_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # ...
     # Password Reset URLs
    path('users/password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
        name='password_reset'),
    path('users/password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(), 
        name='password_reset_done'),
    path('users/reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('users/reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
        name='password_reset_complete'),
]

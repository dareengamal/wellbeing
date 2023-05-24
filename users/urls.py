# AUTH_USER_MODEL = 'users.User'
# AUTHENTICATION_BACKENDS = [
#     'users.backends.RoleBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]

from django.urls import path
from users import views
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    #  path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name='register'),

     path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]


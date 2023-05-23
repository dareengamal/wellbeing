# AUTH_USER_MODEL = 'users.User'
# AUTHENTICATION_BACKENDS = [
#     'users.backends.RoleBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]

from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # Other URLs for your app
#    path('register/customer/', views.register_customer, name='register_customer'),
    # path('register/coach/', views.register_coach, name='register_coach'),
]

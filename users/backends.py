from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

# class RoleBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         User = get_user_model()
#         try:
#             user = User.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         User = get_user_model()
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None

# class RoleBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, role=None, **kwargs):
#         print("RoleBackend is being used!")
#         User = get_user_model()
#         try:
#             user = User.objects.get(username=username)
#             if user.check_password(password) and user.role == role:
#                 return user
#         except User.DoesNotExist:
#             return None

class RoleBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, role=None, **kwargs):
        print("RoleBackend is being used!")
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) and user.role == role:
                return user
            else:
                return None  # Invalid credentials or incorrect role
        except User.DoesNotExist:
            return None

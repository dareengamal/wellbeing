from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

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

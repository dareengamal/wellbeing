from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The Username field must be set.")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTOMER = "CUSTOMER", "Customer"
        COACH = "COACH", "Coach"

    role = models.CharField(max_length=50, choices=Role.choices)

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)  # Hash the password
        return super().save(*args, **kwargs)


class Customer(User):
    base_role = User.Role.CUSTOMER

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for customer"


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.IntegerField(null=True, blank=True)


class Coach(User):
    base_role = User.Role.COACH

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for coach"


class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Customer)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(user=instance)


@receiver(post_save, sender=Coach)
def create_coach_profile(sender, instance, created, **kwargs):
    if created:
        CoachProfile.objects.create(user=instance)




from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTOMER = "CUSTOMER", "Customer"
        COACH = "COACH", "Coach"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:  #if user have no primary key mean is not created
            self.role = self.base_role
            return super().save(*args, **kwargs)

# it just ilter users  with role customer
class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)


class Customer(User):

    base_role = User.Role.CUSTOMER

    Customer = CustomerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for customer"


@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.IntegerField(null=True, blank=True)
 

class CoachManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.COACH)


class Coach(User):

    base_role = User.Role.COACH

    Coach = CoachManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for coach"


class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Coach_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Coach)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "COACH":
        CoachProfile.objects.create(user=instance)
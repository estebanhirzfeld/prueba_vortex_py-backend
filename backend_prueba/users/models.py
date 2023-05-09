from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from roles.models import Roles
# Create your models here.

# class UserManager(BaseUserManager):
#     def _create_user(self, name, email,lastname, password, role, **extra_fields):
#         user = self.model(
            
#             email = email,
#             name = name,
#             lastname = lastname,
#             role = role,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_user(self, email, name,lastname, password=None, **extra_fields):
#         return self._create_user( email, name,lastname, password,  1, **extra_fields)

#     def create_superuser(self, email, name,lastname, password=None, **extra_fields):
#         return self._create_user( email, name,lastname, password, 1, **extra_fields)
class User(models.Model):

    name = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=100, unique=True, null=False)    
    password = models.CharField(max_length=200, null=False)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    # objects = UserManager()


    def __str__(self):
        return f'{self.name} {self.lastname}'
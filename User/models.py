from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class AppUserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff True'))
        
        return self.create_user(email, password, **extra_fields)



class AppUser(AbstractUser):

    username = None
    name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    tokens = models.IntegerField(default=200)
    password = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = AppUserManager()
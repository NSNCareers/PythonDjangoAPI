from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps work with our custom user model"""

    def create_user(self, email, firstName, lastName,password=None):

        if not email:
            raise ValueError('Users must provide a valid email address')
        email = self.normalize_email(email)
        user  = self.model(email=email,firstName=firstName,lastName=lastName)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstName, lastName,password):
        """Creates a new super user"""
        user = self.create_user(email, firstName, lastName,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Represents a "User profile" in our system."""

    email = models.EmailField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName','lastName']

    def get_FullName(self):
        """Used in getting users full name"""

        return self.firstName+''+self.lastName

    def get_FirstName(self):
        """Used in getting users first name"""

        return self.firstName

    def __str__(self):
        """This is used in converting an object to a string"""

        return self.email

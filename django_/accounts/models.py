from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


# User MANAGER Model
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username, email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        # user.is_admin = True
        user.save(using=self._db)
        return user


#  NORMAL User Model : 
class User(AbstractUser, PermissionsMixin):
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'),)
    email = models.EmailField(unique=True)

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    phone = models.CharField(max_length=11,blank=True)
    picture = models.ImageField(upload_to="accounts/images/%Y/%m/%d/%H/%M/%S/", null=True, default="/media/accounts/images/annon.png")
    birthdate = models.DateField(null=True,blank=True)
    profile_url = models.URLField(null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    # objects = UserManager()
    def get_profile_picture(self):
        if self.picture:
            return self.picture.url
        return "/media/accounts/images/annon.png"
    
    def __str__(self) -> str:
        return self.username
    
    @property
    def full_name(self):
        if self.first_name:
            return self.first_name + " " + self.last_name
        return self.username
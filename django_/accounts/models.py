from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'),)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    phone = models.CharField(max_length=11,blank=True)
    picture = models.ImageField(upload_to="account/images/%Y/%m/%d/%H/%M/%S/", null=True, default="/media/accounts/images/annon.png")
    created_at = models.DateField(auto_now_add=True)
    birthdate = models.DateField(null=True,blank=True)
    profile_url = models.URLField(null=True,blank=True)

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
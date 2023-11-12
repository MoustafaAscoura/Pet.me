import datetime

from django.db import models
from django.utils import timezone

class Pet(models.Model):
    TYPE_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField('Name' , max_length=100)
    brief = models.TextField(null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    pet_type = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True)
    species = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=20, null=True)
    birthdate = models.DateField(default=datetime.date.today,null=True)
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return self.name
    
    def get_thumbnail(self):
        try:
            return self.photos.all().first().photo.url
        except:
            return None
        

    def get_age(self):
        if self.birthdate:
            age =  timezone.now().date() - self.birthdate
            y = age.days // 365.25
            m = (age.days % 365.25) // 30
            d = age.days % 30
            return {'years':y,'months':m, 'days':d}
        return {'years':1,'months':0, 'days':0}
    
    class Meta:
        unique_together = ('owner', 'name','birthdate',)

class Photo(models.Model):
    photo = models.ImageField(upload_to="pets/images/%Y/%m/%d/%H/%M/%S/", null=True, blank=True)
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE, related_name='photos')

class Adoption(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='adoptions')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoptions')
    start_at = models.DateField(auto_now_add=True)
    end_at = models.DateField(null=True)

    def __str__(self):
        return f"{self.user} adopted {self.pet}"

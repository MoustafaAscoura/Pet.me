import datetime

from django.db import models
from django.utils import timezone

class Pet(models.Model):
    TYPE_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Turtle', 'Turtle'),
        ('Hamster', 'Hamster'),
        ('Other', 'Other'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField('Name' , max_length=100)
    brief = models.TextField(null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    species = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True)
    breed = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=20, null=True)
    birthdate = models.DateField(default=datetime.date.today,null=True)
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='pets')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_thumbnail(self):
        try:
            return self.photos.all().first().photo.url
        except:
            return None
        

    def get_age(self):
        if self.birthdate:
            res = ""
            age =  timezone.now().date() - self.birthdate
            y = age.days // 365.25
            if y: res += f"{int(y)} years"
            
            m = (age.days % 365.25) // 30
            if m:res += f" {int(m)} months "
            
            d = age.days % 30
            if d and not y: res += f"{int(d)} days"
            
            return res
        
        return
    
    class Meta:
        unique_together = ('owner', 'name','birthdate',)
        ordering = ['-created_at']

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

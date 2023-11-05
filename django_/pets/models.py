from django.db import models

# Create your models here.
class Pet(models.Model):
    TYPE_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(_('Name'), max_length=100)
    brief = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    pet_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    pictures = models.ImageField(upload_to='pet_pictures/')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Adoption(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user} adopted {self.pet}"

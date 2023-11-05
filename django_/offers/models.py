from django.db import models
from accounts.models import User
from pets.models import Pet

# Create your models here.
class Offer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    pet=models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="offers")
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

class AdoptRequest(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    offer=models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="requests")
    created_at = models.DateTimeField(auto_now_add=True)


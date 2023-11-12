from django.db import models
from accounts.models import User
from pets.models import Pet
from chats.models import Message

# Create your models here.
class Offer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="offers")
    pet=models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="offers")
    description=models.TextField(default="")
    created_at = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'pet',)

class AdoptRequest(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    offer=models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="requests")
    message=models.OneToOneField('chats.Message', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'offer',)

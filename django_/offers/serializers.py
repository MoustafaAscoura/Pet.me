from rest_framework import serializers
from .models import Offer,AdoptRequest

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class AdoptRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptRequest
        fields = '__all__'
        #set depth = 1
        
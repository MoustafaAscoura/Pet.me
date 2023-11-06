from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone
from rest_framework import viewsets
from .models import Offer,AdoptRequest
from pets.models import Adoption
from .serializers import OfferSerializer,AdoptRequestsSerializer

# Create your views here.
class OffersView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def perform_create(self, serializer):
        pass
        

class AdoptRequestsView(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = AdoptRequest.objects.filter(offer__id=self.kwargs['id'])

    serializer_class = AdoptRequestsSerializer

    def accept(self, request):
        adopt_request = self.get_object()
        adopt_offer = adopt_request.offer
        pet = adopt_offer.pet
        owner = pet.owner
        adoption = pet.adoptions.last()

        #end ownership of old owner and create new adoption for new owner
        adoption.end_date = timezone.now().date()
        pet.owner = adopt_request.user
        adopt_offer.available = False
        adopt_request.delete()
        new_adoption = Adoption(user=adopt_request.user, pet=pet)
        new_adoption.save()
        return Response('Accepted Adopt Request', status=status.HTTP_204_NO_CONTENT)

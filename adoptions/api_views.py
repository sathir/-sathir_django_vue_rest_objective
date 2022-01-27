from rest_framework.generics import ListAPIView, GenericAPIView
from adoptions.models import Pet
from adoptions.serializers import PetSerializer

class PetList(ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
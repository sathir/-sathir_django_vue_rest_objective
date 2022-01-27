from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from adoptions.models import Pet
from adoptions.serializers import PetSerializer

class PetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class PetList(ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    pagination_class = PetPagination
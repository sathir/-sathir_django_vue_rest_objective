from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from adoptions.models import Pet
from adoptions.serializers import PetSerializer

class PetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class PetList(ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    pagination_class = PetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description')

class PetCreate(CreateAPIView):
    serializer_class = PetSerializer
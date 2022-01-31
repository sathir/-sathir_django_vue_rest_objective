from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
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

class PetRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    lookup_field = 'id'
    serializer_class = PetSerializer

    def delete(self, request, *args, **kwargs):
        pet_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('pet_data_{}'.format(pet_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            pet = response.data
            cache.set('pet_data_{}'.format(pet['id']), {
                'name' : pet['name'],
                'submitter' : pet['submitter'],
                'species' : pet['species'],
                'breed' : pet['breed'],
                'description' : pet['description'],
                'sex' : pet['sex'],
                'submission_date' : pet['submission_date'],
                'age' : pet['age'],
                'vaccinations' : pet['vaccinations'],
            })
        return response
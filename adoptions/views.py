from django.shortcuts import render
from django.http import HttpResponse

from adoptions.models import Pet

def home(request):
    pets = Pet.objects.all()
    return HttpResponse('<p>home view</p>')

def pet_detail(request, pet_id):
    return HttpResponse('<p>pet_detail view with id {pet_id} </p>')
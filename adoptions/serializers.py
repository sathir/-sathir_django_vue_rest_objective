from rest_framework import serializers
from adoptions.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            'id', 'name', 'submitter', 'species', 'breed', 'description',
            'sex', 'submission_date', 'age', 'vaccinations',
        )
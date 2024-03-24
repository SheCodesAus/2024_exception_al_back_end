from rest_framework import serializers
from .models import Workshop  # Import the Workshop model from the models.py file

class WorkshopSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.id')
    class Meta:
        model = Workshop
        fields = '__all__'  # This will serialize all the fields in the Workshop model
        extra_kwargs = {
            'created_by': {'read_only': True},
            
        }
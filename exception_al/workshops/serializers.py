from rest_framework import serializers
from .models import Workshop  # Import the Workshop model from the models.py file

class WorkshopSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Workshop
        fields = '__all__'  # This will serialize all the fields in the Workshop model
        

def create(self, validated_data):
    return Workshop.objects.create(**validated_data)        

def some_view_function(request):
    serializer = WorkshopSerializer(data=request.data, context={'request': request})
    # Rest of your view function code


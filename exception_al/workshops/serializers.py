from rest_framework import serializers
from .models import Workshop  # Import the Workshop model from the models.py file

class WorkshopSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
<<<<<<< HEAD
    class Meta:
        model = Workshop
        fields = '__all__'  # This will serialize all the fields in the Workshop model
        

def create(self, validated_data):
    return Workshop.objects.create(**validated_data)        

def some_view_function(request):
    serializer = WorkshopSerializer(data=request.data, context={'request': request})
    # Rest of your view function code

    created_by = serializers.ReadOnlyField(source='created_by.id')
    class Meta:
        model = Workshop
        fields = '__all__'  # This will serialize all the fields in the Workshop model
        extra_kwargs = {
            'created_by': {'read_only': True},
            
        }
=======
    class Meta:
        model = Workshop
        fields = '__all__'  # This will serialize all the fields in the Workshop model
        

def create(self, validated_data):
    return Workshop.objects.create(**validated_data)        

def some_view_function(request):
    serializer = WorkshopSerializer(data=request.data, context={'request': request})
    # Rest of your view function code

>>>>>>> 09fb8f9 ( resolving merge conflict for PR#6)

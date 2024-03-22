from rest_framework import serializers
from .models import Workshop  # Import the Workshop model from the models.py file

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'  # This will serialize all the fields in the Workshop model

    # This method will be called when we want to create a new workshop
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        workshop = Workshop.objects.create(created_by=user, **validated_data)
        return workshop
# This is the serializer for the Workshop model. It will be used to serialize the Workshop model data into JSON format.
# The WorkshopSerializer class inherits from the ModelSerializer class provided by the Django REST framework.
# The WorkshopSerializer class has a Meta class that specifies the model and the fields to be serialized.
# The create method is overridden to set the created_by field of the Workshop model to the user who is creating the workshop.
# The request object is obtained from the context and the user is obtained from the request object.
# The Workshop object is then created with the created_by field set to the user and the other fields set to the validated data.
# The Workshop object is returned as the result of the create method.
    
    
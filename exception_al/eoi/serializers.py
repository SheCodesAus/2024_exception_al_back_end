from rest_framework import serializers
from .models import Eoi

class EoiSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Eoi
        fields ='__all__'


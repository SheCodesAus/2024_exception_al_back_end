from rest_framework import serializers
from .models import Eoi

class EoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eoi
        fields ='__all__'
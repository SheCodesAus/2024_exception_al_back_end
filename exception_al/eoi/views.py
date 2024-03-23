from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Eoi
from .serializers import EoiSerializer

class EoiList(APIView):

    def get(self, request):
        eoi = Eoi.objects.all()
        serializer = EoiSerializer(eoi, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomEoiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







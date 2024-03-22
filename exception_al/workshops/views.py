from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Workshop
from .serializers import WorkshopSerializer
from django.http import Http404
from rest_framework import status

# Create your views here.
# This is the view for creating a new workshop

class WorkshopCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = WorkshopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    
    
# This is the view for getting a list of all workshops
    
class WorkshopListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data)

class WorkshopDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, workshop_id):
        try:
            return Workshop.objects.get(pk=workshop_id)
        except Workshop.DoesNotExist:
            raise Http404("Workshop does not exist")

    def get(self, request, pk, format=None):
        workshop = self.get_object(pk)
        serializer = WorkshopSerializer(workshop)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        workshop = self.get_object(pk)
        serializer = WorkshopSerializer(workshop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

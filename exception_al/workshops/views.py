from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Workshop
from .serializers import WorkshopSerializer
from django.http import Http404
from rest_framework import status, permissions, viewsets
 


# Create your views here.
# This is the view for creating a new workshop


# This is the view for getting a list of all workshops
    
class WorkshopListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data)


   
    
    def post(self, request):
        serializer = WorkshopSerializer(data=request.data, context={'request': request} )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# This is the view for getting a single workshop by id    

class WorkshopDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, request, workshop_id):
        try:
            return Workshop.objects.get(pk=workshop_id)
        except Workshop.DoesNotExist:
            raise Http404("Workshop does not exist")

    def get(self, request, pk):
        workshop = self.get_object(pk)
        serializer = WorkshopSerializer(workshop)
        return Response(serializer.data)

    def put(self, request, pk):
        workshop = self.get_object(pk)
        serializer = WorkshopSerializer(workshop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# This is the view for getting a list of workshops by category
    
class WorkshopViewSet(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    

    def list(self, request, workshop_category=None):
        if workshop_category:
            workshops = Workshop.objects.filter(category=workshop_category)
        else:
            workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
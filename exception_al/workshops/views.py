from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Workshop
from .serializers import WorkshopSerializer
from django.http import Http404
from rest_framework import status, viewsets
from .permissions import IsSuperuserOrOwnerOrReadOnly
 
# This is the view for getting a list of all workshops
class WorkshopListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkshopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    
# This is the view for getting a single workshop by id    

class WorkshopDetailView(APIView):
    permission_classes = [IsSuperuserOrOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            workshop = Workshop.objects.get(pk=pk)
            self.check_object_permissions(self.request, workshop)
            return workshop
        except Workshop.DoesNotExist:
            raise Http404("Workshop does not exist")

    def get(self, response, pk):
        workshop = self.get_object(pk)
        serializer = WorkshopSerializer(workshop)
        return Response(serializer.data)
    
    def put(self, request, pk):
        workshop = self.get_object(pk)
        serializer = WorkshopSerializer(
            instance=workshop,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk):
        workshop = self.get_object(pk)
        workshop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# This is the view for getting a list of workshops by category
    
class WorkshopViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    

    def list(self, request, workshop_category=None):
        if workshop_category:
            workshops = Workshop.objects.filter(category=workshop_category)
        else:
            workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
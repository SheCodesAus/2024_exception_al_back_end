
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from django.http import Http404
from .models import Eoi
from .serializers import EoiSerializer
from .permissions import IsOwnerOrReadOnly


class EoiList(APIView):
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        eoi = Eoi.objects.all()
        serializer = EoiSerializer(eoi, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EoiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        eoi = self.get_object(pk)
        if not request.user == eoi.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        eoi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EoiDetailView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            eoi = Eoi.objects.get(pk=pk)
            self.check_object_permissions(self.request, eoi)
            return eoi
        except Eoi.DoesNotExist:
            raise Http404("Workshop does not exist")

    def delete(self, request, pk):
        eoi = self.get_object(pk)
        eoi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Eoi
from .serializers import EoiSerializer
from .permissions import IsOwnerOrReadOnly


class EoiList(APIView):
    permission_classes= [IsOwnerOrReadOnly]
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




from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Adverts
from .serializers import AdvertsSerializer

class AdvertListCreate(generics.ListCreateAPIView):
    queryset = Adverts.objects.all()
    serializer_class = AdvertsSerializer

class AdvertRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Adverts.objects.all()
    serializer_class = AdvertsSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return Response({"detail": "DELETE operation not allowed for this resource.", "status_code": status.HTTP_405_METHOD_NOT_ALLOWED}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

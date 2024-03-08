from django.shortcuts import render
from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer
from rest_framework.exceptions import NotFound

class PropertyListCreate(generics.ListCreateAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = Property.objects.all()
        id = self.request.query_params.get('id')
        if id:
            queryset = queryset.filter(id=id)
            if not queryset.exists():
                queryset = Property.objects.filter(property_code=id)
                if not queryset.exists():
                    raise NotFound("Property not found")
        return queryset

class PropertyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'id' 

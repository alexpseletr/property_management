from rest_framework import serializers
from .models import Adverts

class AdvertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adverts
        fields = '__all__'

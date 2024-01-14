# carsapp/serializers.py

from rest_framework import serializers
from .models import Car, User

class CarSerializer(serializers.HyperlinkedModelSerializer):
    
    
    class Meta:
        model = Car
        fields = '__all__'


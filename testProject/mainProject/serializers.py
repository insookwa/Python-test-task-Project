from .models import City , Street , Shop
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist




class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):

     class Meta:
        model = Shop
        fields = '__all__'






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
    # city = CitySerializer(read_only = True)
    # Street = StreetSerializer(read_only = True)
     class Meta:
        model = Shop
        fields = '__all__'


class ShopSearchSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=128)
    street = serializers.CharField(max_length=128)



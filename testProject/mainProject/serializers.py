from .models import City , Street , Shop
from rest_framework import serializers
from datetime import datetime


#http://127.0.0.1:8000/city 
class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = '__all__'

#http://127.0.0.1:8000/city/street
class StreetSerializer(serializers.ModelSerializer):

    city = CitySerializer()

    class Meta:
        model = Street
        fields = ['name','city']


#http://127.0.0.1:8000/shops 
class ShopSerializer(serializers.ModelSerializer):

     city= CitySerializer()
     street = StreetSerializer()

     class Meta:
        model = Shop
        fields = ['name','house','opening_time','closing_time','city','street']

class PostShopSerializer(serializers.ModelSerializer):
 
     class Meta:
        model = Shop
        fields = '__all__'

#http://127.0.0.1:8000/shop/?city=1&street=3&open=1
class ShopSearchSerializer(serializers.ModelSerializer):
    isOpen = serializers.SerializerMethodField('timeDifference')
    city= serializers.CharField(source='city.name')
    street = serializers.CharField(source='street.name')

    def timeDifference(self,obj):
        opening_time = obj.opening_time
        closing_time = obj.closing_time
        shopStatus = "закрытый"
        now = datetime.now()
        requestTime = now.time()
        if requestTime < closing_time and requestTime >opening_time:
            shopStatus = "открывать"
            return shopStatus
        else:   
            return shopStatus
    
    class Meta:
        model = Shop
        fields =['name','city','street','house','opening_time','closing_time','isOpen']



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
    city_name= serializers.SerializerMethodField(source = 'get_city_name')
    def get_city_name(self, obj):
        return obj.city.name
    class Meta:
        model = Street
        fields = ['name','city_name']


#http://127.0.0.1:8000/shops 
class ShopSerializer(serializers.ModelSerializer):
     city_name= serializers.SerializerMethodField(source = 'get_city_name')
     street_name = serializers.SerializerMethodField(source= 'get_street_name')

     def get_city_name(self, obj):
        return obj.city.name

     def get_street_name(self, obj):
        return obj.street.name
 
     class Meta:
        model = Shop
        fields = ['name','house','opening_time','closing_time','city_name','street_name']

class PostShopSerializer(serializers.ModelSerializer):
 
     class Meta:
        model = Shop
        fields = '__all__'




#http://127.0.0.1:8000/shop/?city=1&street=3&open=1
class ShopSearchSerializer(serializers.ModelSerializer):
    isOpen = serializers.SerializerMethodField('timeDifference')
    city_name= serializers.SerializerMethodField(source = 'get_city_name')
    street_name = serializers.SerializerMethodField(source= 'get_street_name')

    def get_city_name(self, obj):
        return obj.city.name

    def get_street_name(self, obj):
        return obj.street.name

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
        fields =['name','city_name','street_name','house','opening_time','closing_time','isOpen']



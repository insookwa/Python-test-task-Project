from .models import Shop , Street , City
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
#from tkinter.tix import Tree
from .filters import shopSearchFilter


#http://127.0.0.1:8000/shops :Это возвращает при вызове метода get и добавляет магазин при завершении публикации
class ShopsApiView(APIView):

    def get(self,request,format=None):
        response  = Shop.objects.all()
        serializer =ShopSerializer(response ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.data.get('name'),
                'city' : request.data.get('city'),
                'street' : request.data.get('street'),
                'house' : request.data.get('house'),
                'opening_time' : request.data.get('opening_time'),
                'closing_time' : request.data.get('closing_time'),        
        }

        serializer = PostShopSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#http://127.0.0.1:8000/shop/?city=1&street=3&open=1 Это возвращает магазины в выбранном городе с указанием того, открыты они или закрыты
class ShopSearchView(APIView):

    def get(self,request,format=None):
        street = self.request.query_params.get('street',None)
        city = self.request.query_params.get('city',None)
        open = self.request.query_params.get('open',None)

        return shopSearchFilter(open,city,street)




#http://127.0.0.1:8000/city Это возвращает и добавляет город
class CityApiView(APIView):

    def get(self,request,format=None):
        
        response = City.objects.all()
        serializer = CitySerializer(response,many=True)
        return Response(serializer.data)
        
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.data.get('name'),
        }

        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#http://127.0.0.1:8000/city/street Это возвращает все улицы и может добавить улицу с помощью метода post

class StreetApiView(APIView):
    def get(self, request,format=None):
        response = Street.objects.all()
        serializer = StreetSerializer(response,many=Tree)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.data.get('name'),
                'city' : request.data.get('city')

        }

        serializer = StreetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











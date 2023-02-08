from django.shortcuts import render
from .models import Shop , Street , City
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from tkinter.tix import Tree
from rest_framework import filters
from .filters import DynamicSearchFilter
from rest_framework.generics import ListCreateAPIView


class ShopsApiView(APIView):



    def get(self,request,format=None):
        response  = Shop.objects.all()
        serializer =ShopSerializer(response ,many=Tree)
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

        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityApiView(APIView):

    def get(self,request,format=None):
        
        response = City.objects.all()
        serializer = CitySerializer(response,many=Tree)
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

class PostShopSearchView(APIView):

    def post(self,request,format=None):
        serializer = ShopSearchSerializer(data=request.data)
        city = request.data.get('city'),
        street = request.data.get('street')

        shops = Shop.objects.filter(city__name__icontains = city,street__name__icontains = street)
        serializer =ShopSerializer(shops ,many=Tree)
        return Response(serializer.data,status=status.HTTP_200_OK)


class ShopSearchView(APIView):
   
   def get(self,request,format=None):
    city = self.request.query_params.get('city',None)
    street = self.request.query_params.get('street',None)
    response = Shop.objects.filter(city = city, street = street)
    serializer = ShopSerializer(response,many=Tree)
    return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionsAPIView(ListCreateAPIView):
    search_fields = ['city','street']
    filter_backends = (filters.SearchFilter,)
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
from django.shortcuts import render
from .models import Shop , Street , City
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tkinter.tix import Tree

class ShopsApiView(APIView):

    def get(self,request,format=None):

        name = self.request.query_params.get('name',None)
        city = self.request.query_params.get('city',None)
        street = self.request.query_params.get('street',None)
        house =  self.request.query_params.get('house',None)
        opening_time = self.request.query_params.get('opening_time',None)
        closing_time=self.request.query_params.get('closing_time',None)

        response  = Shop.objects.all()
        serializer =ShopSerializer(response ,many=Tree)
        return Response(serializer.data)

        
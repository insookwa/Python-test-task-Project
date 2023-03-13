from .models import Shop 
from datetime import datetime
from .serializers import *
from rest_framework.response import Response
#from tkinter.tix import Tree
from rest_framework import status 
       

def shopSearchFilter(isopen,city,street):

        now = datetime.now()
        requestTime = now.time()
        print(requestTime)
        response = Shop.objects.filter(street=street,city = city)
        isopen = int(isopen)


        if isopen == 1:   
            filterOpen =response.filter(opening_time__lte=requestTime)
            print(filterOpen)
            finalOpenFilter = filterOpen.filter(closing_time__gte=requestTime)
            serializer = ShopSearchSerializer(finalOpenFilter,many = True)  
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif isopen == 0:
            filterClosed =response.filter(closing_time__gte=requestTime)
            print(filterClosed)
            finalClosedFilter = filterClosed.filter(opening_time__gte=requestTime)
            print(finalClosedFilter.values() )
            serializer = ShopSearchSerializer(finalClosedFilter,many = True)
            print(serializer.data)
            return Response(serializer.data)
        else:
            serializer = ShopSearchSerializer(response,many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)


            
from django import urls
from django.urls import path, include
from rest_framework import routers
from .views import *
from django import views

urlpatterns = [

    path('shops',ShopsApiView.as_view(),name='all-shops'),
    path('shop/',ShopSearchView.as_view(),name='shop'),
    path('city',CityApiView.as_view(),name='all-cities' ),
    path('city/street',StreetApiView.as_view(),name='all-streets' ),



]

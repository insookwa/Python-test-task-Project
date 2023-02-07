from django.urls import path, include
from rest_framework import routers
from .views import *
from django import views


urlpatterns = [
    path('',ShopsApiView.as_view(),name='all-data')
]

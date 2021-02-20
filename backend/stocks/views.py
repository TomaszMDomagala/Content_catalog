from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import StockSerializer, StockTypeSerializer  
from .models import Stock, StockType

class StockView(viewsets.ModelViewSet):
  serializer_class = StockSerializer
  queryset = Stock.objects.all()

class StockTypeView(viewsets.ModelViewSet):
  serializer_class = StockTypeSerializer
  queryset = StockType.objects.all()
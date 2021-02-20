from .models import Stock, StockType
from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):
  class Meta:
    model = Stock
    fields = ('id', 'name', 'stock_name', 'date_added', 'amount', 'value_at_buy', 'type_of_stock')

class StockTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = StockType
    fields = ('name_of_type', )
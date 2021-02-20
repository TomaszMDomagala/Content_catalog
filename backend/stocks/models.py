from django.db import models
from django.urls import reverse
import uuid

class StockType(models.Model):
    name_of_type    = models.CharField(max_length=40, help_text='Enter type of stock that you own')

    def __str__(self):
        return self.name_of_type

class Stock(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular stock')
    name            = models.CharField(max_length=100, help_text='Enter name of the stock')
    stock_name      = models.CharField(max_length=20, help_text='Enter your symbol')
    date_added      = models.DateTimeField(null=True, blank=True)
    amount          = models.DecimalField(max_digits=20, decimal_places=8)
    value_at_buy    = models.DecimalField(max_digits=20, decimal_places=2)
    type_of_stock   = models.ManyToManyField(StockType, help_text='Select type of this stock')

    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.stock_name

    def get_absolute_url(self):
        return reverse('stock-detail', args=[str(self.id)])

    def display_type(self):
        return ', '.join(type_of_stock.name_of_type for type_of_stock in self.type_of_stock.all()[:3])

    display_type.short_description = "Type"


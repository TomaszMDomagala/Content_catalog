from django.contrib import admin
from .models import Stock, StockType

admin.site.register(StockType)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_name', 'amount', 'value_at_buy', 'date_added', 'display_type')
    list_filter = ('type_of_stock', 'date_added')

    fieldsets = (
        ('Names', {
            'fields': ('name', 'stock_name', 'date_added')
        }),
        ('Statistics', {
            'fields': [('amount', 'value_at_buy'), 'type_of_stock']
        }),
    )
    
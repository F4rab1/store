from typing import Any
from django.contrib import admin
from . import models
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        url = (
            reverse('admin:store_product_changelist') 
            + '?' 
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{}</a>', url, collection.product_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('product')
        )
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 5
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment_status', 'customer_fullname']
    list_per_page = 10
    list_select_related = ['customer']

    def customer_fullname(self, order):
        return order.customer.first_name + ' ' + order.customer.last_name
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
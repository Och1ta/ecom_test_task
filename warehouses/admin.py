from django.contrib import admin
from .models import Category, Stock, Equipment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    search_fields = ['name', 'location']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['category', 'stock']


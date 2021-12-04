from django.contrib import admin
from .models import Medicine, Pharmacy, AvailabilityOfMedicines, Category


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'volume', 'manufacturer', 'is_recipe_need','category','price')
    list_display_links = ('name', 'manufacturer')
    search_fields = ('name', 'manufacturer', 'is_recipe_need', 'category')


class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('address', 'number', 'nearest_metro')
    list_display_links = ('address', 'number')
    search_fields = ('number', 'nearest_metro')


class AvailabilityOfMedicinesAdmin(admin.ModelAdmin):
    list_display = ('pharmacy', 'medicine', 'count')
    list_display_links = ('pharmacy', 'medicine')
    search_fields = ('pharmacy', 'medicine')


admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(AvailabilityOfMedicines, AvailabilityOfMedicinesAdmin)
admin.site.register(Category)

# -*- coding: utf-8 -*-
from django.db import models

class Pharmacy(models.Model):
    address = models.CharField(max_length=150, verbose_name='Адрес')
    number = models.CharField(max_length=50, verbose_name='Номер')
    nearest_metro = models.CharField(max_length=50, verbose_name='Ближайшая станция метро', db_index=True)

    def __str__(self):
        return self.address +" " + self.number + " " + self.nearest_metro

class Category(models.Model):
    name = models.CharField(max_length=50,  verbose_name='Название')

    def __str__(self):
        return  self.name

class Medicine(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    dosage = models.CharField(max_length=50,  verbose_name='Дозировка')
    volume = models.CharField(max_length=50, verbose_name='Объем', db_index=True)
    manufacturer = models.CharField(max_length=50,  verbose_name='Производитель')
    is_recipe_need = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class AvailabilityOfMedicines(models.Model):
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.DO_NOTHING)
    medicine = models.ForeignKey(Medicine,on_delete=models.DO_NOTHING)
    count = models.IntegerField(null=True, blank=True)


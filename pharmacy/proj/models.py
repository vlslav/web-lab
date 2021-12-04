from django.db import models


class Pharmacy(models.Model):
    address = models.CharField(max_length=150, verbose_name='Адрес')
    number = models.CharField(max_length=50, verbose_name='Номер')
    nearest_metro = models.CharField(max_length=50, verbose_name='Ближайшая станция метро', db_index=True)

    def __str__(self):
        return "Aптека " + self.address + " " + self.number + " " + "Ближайшая станция метро: " + self.nearest_metro

    class Meta:
        verbose_name_plural = 'Аптеки'
        verbose_name = 'Аптека'
        ordering = ['-number']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категория'
        verbose_name = 'Категория'
        ordering = ['name']


class Medicine(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название', db_index=True)
    dosage = models.CharField(max_length=50,  verbose_name='Дозировка')
    volume = models.CharField(max_length=50, verbose_name='Объем')
    manufacturer = models.CharField(max_length=50,  verbose_name='Производитель')
    is_recipe_need = models.IntegerField(null=True, blank=True, verbose_name='Необходимость рецепта')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')

    def __str__(self):
        return "Название: "+ self.name + " Производитель: " + self.manufacturer + " Объем: " + self.volume + " Цена(руб): " + self.price.__str__()

    class Meta:
        verbose_name_plural = 'Лекарства'
        verbose_name = 'Лекарство'
        ordering = ['-name']


class AvailabilityOfMedicines(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.DO_NOTHING)
    medicine = models.ForeignKey(Medicine, on_delete=models.DO_NOTHING)
    count = models.IntegerField(null=True, blank=True, verbose_name='Количество')

    class Meta:
        verbose_name_plural = 'Информация о наличии лекарств'
        verbose_name = 'Информация о наличии лекарств'
        ordering = ['-count']


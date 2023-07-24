from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=140, verbose_name="имя")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(verbose_name="изображение")
    category = models.CharField(max_length=140, verbose_name="категория")
    price = models.FloatField(verbose_name="цена")
    creation_date = models.DateField(auto_now_add=True, verbose_name="дата создания")
    date_of_change = models.DateField(auto_now=True, verbose_name="дата последнего изменения")


class Category(models.Model):
    name = models.CharField(max_length=140, verbose_name="имя")
    description = models.TextField(verbose_name="описание")

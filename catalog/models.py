from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=140, verbose_name="имя")
    description = models.TextField(verbose_name="описание")

    # def __str__(self):
    #     return f'{self.id} {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=140, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    price = models.FloatField(verbose_name="цена")
    creation_date = models.DateField(auto_now_add=True, verbose_name="дата создания", **NULLABLE)
    date_of_change = models.DateField(auto_now=True, verbose_name="дата последнего изменения")

    # def __str__(self):
    #     return f'Название: {self.name}\n{self.description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
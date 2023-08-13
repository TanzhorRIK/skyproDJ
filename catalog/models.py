from django.db import models
from django.urls import reverse
from transliterate import translit

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=140, verbose_name="имя")
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=140, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(upload_to="photos/", verbose_name="изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="категория")
    price = models.FloatField(verbose_name="цена")
    creation_date = models.DateField(auto_now_add=True,
                                     verbose_name="дата создания", **NULLABLE)
    date_of_change = models.DateField(auto_now=True,
                                      verbose_name="дата последнего изменения")

    def __str__(self):
        return f'{self.name}\n{self.description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Blog(models.Model):
    name = models.CharField(max_length=140, verbose_name="название")
    slug = models.CharField(max_length=30, verbose_name='слаг', unique=True)
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(upload_to="photos/blog/",
                                verbose_name="изображение", **NULLABLE)
    creation_date = models.DateField(auto_now_add=True,
                                     verbose_name="дата создания", **NULLABLE)
    publication_attribute = models.BooleanField(verbose_name="признак публикации")
    count_views = models.IntegerField(default=0, verbose_name="число просмотров")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:blog", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = translit(self.name, language_code='ru', reversed=True)
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.publication_attribute = False
        self.save()
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, **NULLABLE)
    number = models.IntegerField(verbose_name="Версия", **NULLABLE)
    name = models.CharField(max_length=100, verbose_name="Имя версии", **NULLABLE)
    status = models.BooleanField(verbose_name="Статус", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
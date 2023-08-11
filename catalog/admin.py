from django.contrib import admin

from catalog.models import Category, Product, Blog


# Register your models here.
@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")

@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "content")

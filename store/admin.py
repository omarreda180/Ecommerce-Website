from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther', 'price', 'in_stock', 'is_active', 'created', 'update']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'is_active', 'in_stock']

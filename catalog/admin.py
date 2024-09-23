from django.contrib import admin
from catalog.models import Category, Product, Version
from blog.models import Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'is_published', 'view_counter')
    list_filter = ('is_published',)
    search_fields = ('title',)
    # prepopulated_fields = {'slug': ('pk', 'title',)}


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'number', 'name', 'is_current')
    list_filter = ('is_current',)
    search_fields = ('name', 'product')

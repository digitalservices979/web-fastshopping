from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	readonly_fields = 'product_created', 'product_updated'
	exclude = ('slug_product',)
	list_display = ('name_product','category_product','brand_product')

class CategoryAdmin(admin.ModelAdmin):
	exclude = ('slug_category',)

class BrandAdmin(admin.ModelAdmin):
	exclude = ('slug_brand',)

class ColorAdmin(admin.ModelAdmin):
	exclude = ('slug_color',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Color, ColorAdmin)
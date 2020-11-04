from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #поле заполняется автоматически с помощью другого поля
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    #отображаемые поля
    list_display = ['name', 'slug', 'price', 'stock']
    #изменяемые поля
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

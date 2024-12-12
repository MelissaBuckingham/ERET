from django.contrib import admin
from .models import Product, Category, Image

# Register your models here.

class ImageAdmin(admin.StackedInline):
    model = Image

class ImageAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'imagename',
        'image',
    )

    ordering = ('sku',)

    inlines = [ImageAdmin]

    class Meta:
       model = Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product)
admin.site.register(Category)




admin.site.register(Image)

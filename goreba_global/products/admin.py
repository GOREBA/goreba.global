import admin_thumbnails
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from products.models import Category, Product, Images, Color, Size, Variant, Brand


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Variant)
admin.site.register(Brand)

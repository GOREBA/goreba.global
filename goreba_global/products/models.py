from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Brand(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')

    keywords = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/product')

    is_active = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.CASCADE)

    keywords = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    variants = models.CharField(max_length=10, choices=VARIANTS, default='None')
    detail = RichTextField(blank=True)
    image_main = models.ImageField(upload_to='images/product', null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discounted_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    is_digital = models.BooleanField(default=False)

    is_active = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/product/')

    def __str__(self):
        return self.title


class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Variant(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True, default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.title

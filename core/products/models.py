from django.db import models


class Product(models.Model):
    brand = models.ForeignKey('Brand', verbose_name='Brand', on_delete=models.CASCADE)
    clothes = models.CharField('Type of clothes', max_length=30)
    name_clothes = models.CharField('Full name of clothes', max_length=50)
    price = models.PositiveIntegerField('Price')
    photo = models.ImageField('Image', upload_to='product_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
        db_table = 'Product'

    def __str__(self):
        return f'{self.brand}: {self.name_clothes}'


class Brand(models.Model):
    brand = models.CharField('Brand', max_length=60)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        db_table = 'Brand'

    def __str__(self):
        return f'{self.brand}'


from django.db import models
from tinymce.models import HTMLField
class Sailor(models.Model):
    nickname = models.CharField('Nickname', max_length=50)
    birth_day = models.DateField('Date of birth')

    def __str__(self):
        return self.nickname

class Product(models.Model):
    product_name = models.CharField('Product name', max_length=200)
    seller = models.ForeignKey('Sailor', on_delete=models.CASCADE, blank=True)
    price = models.FloatField('Price', null=True, blank=True, default=None)
    description = HTMLField()
    insDate = models.DateTimeField('Instance date', auto_now_add=True)
    type = models.ManyToManyField('ProductType')
    product_thumbnail = models.ImageField('Thumbnail', upload_to='product_thumbnails', null=True)
    LOAN_STATUS = (
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('t', 'Sold'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Status',
    )
    def __str__(self):
        return (f'{self.product_name} | {self.seller}')
class Service(models.Model):
    service_name = models.CharField('Service name', max_length=200)
    seller = models.ForeignKey('Sailor', on_delete=models.CASCADE, blank=True)
    description = HTMLField()
    type = models.ManyToManyField('ServiceType')
    service_thumbnail = models.ImageField('Thumbnail', upload_to='service_thumbnails', null=True)
    def __str__(self):
        return (f'{self.service_name} | {self.seller}')

class ServiceType(models.Model):
    service_type_name = models.CharField('Type', max_length=50)

    def __str__(self):
        return self.service_type_name
class ProductType(models.Model):
    product_type_name = models.CharField('Type', max_length=50)
    def __str__(self):
        return self.product_type_name




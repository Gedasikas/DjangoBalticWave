from django.db import models
from tinymce.models import HTMLField
class Sailor(models.Model):
    nickname = models.CharField('Nickname', max_length=50)
    birth_day = models.DateField('Date of birth')
class Product(models.Model):
    product_name = models.CharField('Product name', max_length=200)
    seller = models.ForeignKey('Sailor', on_delete=models.CASCADE, blank=True)
    price = models.FloatField('Price', null=True, blank=True, default=None)
    description = HTMLField()
    insDate = models.DateTimeField('Instance date', auto_now_add=True)
    type = models.ManyToManyField('ProductType')
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
class Service(models.Model):
    service_name = models.CharField('Service name', max_length=200)
    seller = models.ForeignKey('Sailor', on_delete=models.CASCADE, blank=True)
    description = HTMLField()
    type = models.ManyToManyField('ProductType')

class ServiceType(models.Model):
    service_type_name = models.CharField('Type', max_length=50)
class ProductType(models.Model):
    product_type_name = models.CharField('Type', max_length=50)





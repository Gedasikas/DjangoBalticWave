from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField('Product name', max_length=200)
    product_seller = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField('Price', null=True, blank=True, default=0)
    short_description = HTMLField('Short description', max_length=200)
    description = HTMLField(default='No description')
    insDate = models.DateTimeField('Instance date', auto_now_add=True)
    type = models.ManyToManyField('ProductType')
    product_thumbnail = models.ImageField('Thumbnail', upload_to='product_thumbnails', null=True, blank=True)
    image1 = models.ImageField('Image 1', upload_to='product_images', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    CITY_CHOICES = [
        ('Klaipėda county', (
            ('KLP', 'Klaipėda'),
            ('PL', 'Palanga'),
            ('NID', 'Nida'),
        )
         ),
        ('Kaunas county', (
            ('KUN', 'Kaunas'),
            ('JON', 'Jonava'),
            ('KĖD', 'Kėdainiai')
        )
         ),
        ('Vilnius county', (
            ('VIL', 'Vilnius'),
            ('UKM', 'Ukmergė'),
            ('ELE', 'Elektrėnai'),

        )
         ),
        ('Šiauliai county', (
            ('ŠL', 'Šiauliai'),
            ('RAD', 'Radviliškis'),
            ('NJA', 'Naujoji Akmenė'),
        )
         ),
        ('UN', 'Undefined'),
    ]

    LOAN_STATUS = (
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('t', 'Sold'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Status',)
    city = models.CharField(max_length=3, choices=CITY_CHOICES, help_text='City', default='UN')

    def display_type(self):
        return ', '.join(type.product_type_name for type in self.type.all()[:3])

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return (f'{self.product_name} | {self.product_seller}')

class Service(models.Model):
    service_name = models.CharField('Service name', max_length=200)
    service_seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = HTMLField(default='No description')
    type = models.ManyToManyField('ServiceType')
    service_thumbnail = models.ImageField('Thumbnail', upload_to='service_thumbnails', null=True, blank=True)
    def __str__(self):
        return (f'{self.service_name}')

class ServiceType(models.Model):
    service_type_name = models.CharField('Type', max_length=50)

    def __str__(self):
        return self.service_type_name
class ProductType(models.Model):
    product_type_name = models.CharField('Type', max_length=50)
    def __str__(self):
        return self.product_type_name

class ProductReview(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='productreview')
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Review', max_length=2000)

    class Meta:
        ordering = ['-date_created']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
    def __str__(self):
        return f'{self.user.username}'




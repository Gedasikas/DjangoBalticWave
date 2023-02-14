from django.contrib import admin

from .models import Sailor, Product, Service, ServiceType, ProductType

admin.site.register(Sailor)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(ServiceType)
admin.site.register(ProductType)

from django.contrib import admin
from .models import Sailor, Product, Service, ServiceType, ProductType


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'seller', 'insDate')
    list_filter = ('status', 'type')
    search_fields = ('product_name', 'seller')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'seller')
    list_filter = ('type',)
    search_fields = ('service_name', 'seller')


class ProductInline(admin.TabularInline):
    model = Product
    readonly_fields = ('product_name', 'description', 'price', 'type', 'status',)
    can_delete = False
    extra = 0


class ServiceInline(admin.TabularInline):
    model = Service
    readonly_fields = ('service_name', 'description', 'type')
    can_delete = False
    extra = 0


class SailorAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'birth_day')
    inlines = [(ProductInline), (ServiceInline)]


admin.site.register(Sailor, SailorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType)
admin.site.register(ProductType)

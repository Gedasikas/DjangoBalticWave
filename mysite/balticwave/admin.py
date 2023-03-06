from django.contrib import admin
from .models import Profile, Product, Service, ServiceType, ProductType, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'insDate', 'display_type',)
    list_filter = ('status', 'type')
    search_fields = ('product_name',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name',)
    list_filter = ('type',)
    search_fields = ('service_name', )


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

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'date_created', 'reviewer', 'content')



admin.site.register(Profile)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType)
admin.site.register(ProductType)
admin.site.register(ProductReview, ProductReviewAdmin)

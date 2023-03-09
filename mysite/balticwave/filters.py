import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    product_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = {
            'city': ['exact'],
            'category': ['exact'],
            'type': ['exact'],
            'status': ['exact'],

        }

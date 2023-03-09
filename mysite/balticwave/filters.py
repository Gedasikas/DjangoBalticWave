import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    product_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = [
            'product_name',
            'city',
            'category',
            'type',
            'status',
        ]

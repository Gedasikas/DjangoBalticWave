from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Product, Service
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class SellerProductsListView(LoginRequiredMixin, generic.ListView):
    Model = Product
    template_name = 'seller_products.html'
    context_object_name = 'myproducts'
    def get_queryset(self):
        return Product.objects.filter(product_seller=self.request.user)

class ServiceListView(generic.ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'

class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'

def search(request):
    query = request.GET.get('query')
    search_results = Product.objects.filter(Q(product_name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'products': search_results, 'query': query})



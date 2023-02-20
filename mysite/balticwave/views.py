from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Product, Service
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
class ServiceListView(generic.ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'

class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'

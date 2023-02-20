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


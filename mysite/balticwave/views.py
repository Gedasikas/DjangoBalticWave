from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import Product, Service
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    template_name = 'my_products.html'
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

class SellerServiceListView(LoginRequiredMixin, generic.ListView):
    Model = Service
    template_name = 'my_services.html'
    context_object_name = 'myservices'
    def get_queryset(self):
        return Service.objects.filter(service_seller=self.request.user)

def search(request):
    query = request.GET.get('query')
    search_results = Product.objects.filter(Q(product_name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'products': search_results, 'query': query})

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:

                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} registered!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def profile(request):
    return render(request, 'profile.html')



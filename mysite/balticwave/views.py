from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import FormMixin
from .models import Product, Service
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, ProductReviewForm, ServiceForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .filters import ProductFilter
from django.urls import reverse
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect



def home(request):
    latest_prod = Product.objects.all().order_by('-id')[:5]
    context = {
    'latest_prod': latest_prod,
    }
    return render(request, 'home.html', context=context)


class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    paginate_by = 10
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class ProductDetailView(FormMixin, generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    form_class = ProductReviewForm

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.product = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(ProductDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Product, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


class SellerProductsListView(LoginRequiredMixin, generic.ListView):
    Model = Product
    template_name = 'my_products.html'
    context_object_name = 'myproducts'
    def get_queryset(self):
        return Product.objects.filter(product_seller=self.request.user)

class SellerProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'my_product.html'
    context_object_name = 'product'

class ProductByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = ['product_name', 'price', 'short_description', 'description', 'type', 'product_thumbnail', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'city', 'status']
    success_url = '/balticwave/myproducts/'
    template_name = 'user_product_form.html'
    def form_valid(self, form):
        form.instance.product_seller = self.request.user
        return super().form_valid(form)

class ProductByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Product
    fields = ['product_name', 'price', 'short_description', 'description', 'type', 'product_thumbnail', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'city', 'status']
    success_url = '/balticwave/myproducts/'
    template_name = 'user_product_form.html'

    def form_valid(self, form):
        form.instance.product_seller = self.request.user
        return super().form_valid(form)
    def test_func(self):
        product = self.get_object()
        return self.request.user == product.product_seller

class ProductByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Product
    success_url = '/balticwave/myproducts/'
    template_name = 'user_product_delete.html'
    context_object_name = 'product'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.product_seller

def product_like(request, pk):
    post = get_object_or_404(Product, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('product-detail', args=[str(pk)]))

@login_required
def favourite_prod_add(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favourite_list(request):
    new = Product.objects.all().filter(favourites=request.user)
    return render(request, 'favourites.html', {'new': new})

@login_required
def advert_list(request):
    username = request.user.username
    product_list = Product.objects.filter(product_seller__username=username)
    service_list = Service.objects.filter(service_seller__username=username)
    context = {'product_list': product_list,
               'service_list': service_list,
    }
    return render(request, 'advert_list.html', context)

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
    search_results2 = Service.objects.filter(Q(service_name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'products': search_results, 'services': search_results2, 'query': query})


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
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)



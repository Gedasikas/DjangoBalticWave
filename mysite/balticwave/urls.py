from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-like/<int:pk>', views.product_like, name="product_like"),
    path('favouriteproducts/<int:pk>', views.favourite_prod_add, name='favourite-prod-add'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),
    path('search/', views.search, name='search'),
    path('myadverts/', views.advert_list, name='advert-list'),
    path('myproducts/', views.SellerProductsListView.as_view(), name='my-products'),
    path('myproducts/new', views.ProductByUserCreateView.as_view(), name='my-new-product'),
    path('myproducts/<int:pk>/update', views.ProductByUserUpdateView.as_view(), name='my-update-product'),
    path('myproducts/<int:pk>/delete', views.ProductByUserDeleteView.as_view(), name='my-delete-product'),
    path('myproducts/<int:pk>', views.SellerProductDetailView.as_view(), name='my-product'),
    path('myservices/', views.SellerServiceListView.as_view(), name='my-services'),
    path('myfavourites/', views.favourite_list, name='favourite-list'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
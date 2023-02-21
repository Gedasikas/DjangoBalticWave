from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),
    path('search/', views.search, name='search'),
    path('search/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('myproducts/', views.SellerProductsListView.as_view(), name='my-products'),
    path('myservices/', views.SellerServiceListView.as_view(), name='my-services'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

]
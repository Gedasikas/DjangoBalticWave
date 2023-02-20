from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),
]
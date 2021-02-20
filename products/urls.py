from django.urls import path
from .views import Product_list, ProductDetailView, ProductListView, manufacturer_list, manufacturer_detail

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"), # homepage
    # pages based on primary keys associated ti products 
    path("products/<int:pk>", ProductDetailView.as_view(), name="product-detail"), 
    
    # API usage
    path("products/", Product_list, name="product-api-list"),
    path("manufacturers/", manufacturer_list, name="manufacturer-api-list"),
    path("manufacturers/<int:pk>", manufacturer_detail, name="manufacturer-detail-api")
]
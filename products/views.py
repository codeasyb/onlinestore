# from django.shortcuts import render

# Create your views here.
# you use generic class views in django is the easiest way

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# this library was used for the api purpose
from django.http import JsonResponse
from .models import Manufacturer, Product

class ProductDetailView(DetailView):
    
    model = Product
    template_name = "products/product_detail.html"
    
class ProductListView(ListView):
    
    model = Product
    template_name = "products/product_list.html"
    
# API's 
def Product_list(request):
    products = Product.objects.all()
    data = {
        "products": list(products.values())
    }
    return JsonResponse(data)


def Product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name, 
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity,
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Product not found!"
            }
        }, status=404)
    return response

def manufacturer_list(request):
    # this is to get all of the instances of the manufacturer objects
    manufacturer_all = Manufacturer.objects.all() 
    # this is to find only the active manufacturers
    manufacturer_filter = Manufacturer.objects.filter(active=True)
    data = {
        "manufacturer_all": list(manufacturer_all.values()),
        "manufacturer_filter": list(manufacturer_filter.values())
    }
    return JsonResponse(data)

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {
            "manufacturer": {
                "name": manufacturer.name,
                "location": manufacturer.location, 
                "active": manufacturer.active,
                "products": list(manufacturer_products.values())
            }
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "manufacturer not found!"
            }
        }, status=404)
    return response
 
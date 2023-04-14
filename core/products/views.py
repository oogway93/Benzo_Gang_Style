from django.shortcuts import render
from .models import *

def main(request):
    brand = Brand.objects.all()
    product = Product.objects.all()
    return render(request, 'products/main.html', {'brand': brand, 'products': product})

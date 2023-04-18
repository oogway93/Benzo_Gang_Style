from django.urls import path
from products.views import *

app_name = 'product'

urlpatterns = [
    path('', Base, name='base')
]

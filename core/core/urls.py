from django.contrib import admin
from django.urls import path, include
from .urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('api/', include('api.urls', namespace='api'))

]

from rest_framework import routers
from django.urls import include, path

from api.views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)
# router.register(r'accounts', AccountViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
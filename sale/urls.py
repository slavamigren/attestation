from django.urls import path
from rest_framework import routers

from sale.apps import SaleConfig
from sale.views import SellerSet

app_name = SaleConfig.name

urlpatterns = [

]

router_supplier = routers.SimpleRouter()
router_supplier.register(r'seller', SellerSet, basename='seller')

urlpatterns += router_supplier.urls

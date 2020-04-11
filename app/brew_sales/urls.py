from rest_framework import routers

from .views import SalesItemViewSet

v1_router = routers.SimpleRouter()
v1_router.register('sales_item', SalesItemViewSet, basename='sales_item')

urlpatterns = v1_router.urls

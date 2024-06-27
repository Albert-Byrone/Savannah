from django.urls import include, path
from rest_framework import routers
from .views import CustomerViewSet, OrderViewSet
# from order.views import CustomerViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
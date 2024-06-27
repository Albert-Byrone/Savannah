from rest_framework import viewsets
from .models import Customer, Order
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerSerializer, OrderSerializer
from .utils import send_sms
# from oidc_provider.decorators import protected_resource_view
# from oidc_provider.lib.utils.oauth2 import protected_resource_view





class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAuthenticated]


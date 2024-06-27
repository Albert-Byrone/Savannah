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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()
        send_sms(instance)




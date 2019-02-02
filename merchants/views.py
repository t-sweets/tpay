from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework import generics

from .models import Merchant
from .serializer import MerchantSerializer
from checkouts.serializer import CheckoutSerializer
from checkouts.models import Checkout


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = (IsAdminUser,)


class MerchantAllCheckoutListView(generics.ListAPIView):
    serializer_class = CheckoutSerializer

    def get_queryset(self):
        user = self.request.user
        owner_merchants = user.merchant_set.all()
        return Checkout.objects.filter(merchant=owner_merchants)


class MerchantCheckoutListView(generics.ListAPIView):
    serializer_class = CheckoutSerializer

    def get_queryset(self):
        merchant = self.kwargs['merchant']
        return Checkout.objects.filter(merchant=merchant)

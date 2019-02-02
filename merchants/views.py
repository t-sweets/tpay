from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins

from .models import Merchant
from .serializer import MerchantSerializer
from checkouts.serializer import CheckoutSerializer
from checkouts.models import Checkout


class MerchantViewSet(mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = MerchantSerializer

    def get_queryset(self):
        account = self.request.user
        return Merchant.objects.filter(accounts=account)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


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

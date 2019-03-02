from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins
from django.shortcuts import get_object_or_404

from .models import Merchant
from .serializer import MerchantSerializer
from checkouts.serializer import CheckoutSerializer
from checkouts.models import Checkout


class MerchantViewSet(mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):

    lookup_field = 'id'
    serializer_class = MerchantSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        account = self.request.user
        return Merchant.objects.filter(accounts=account)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class MerchantAllCheckoutListView(generics.ListAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        account = self.request.user
        merchants = account.merchant_set.all()
        return Checkout.objects.filter(merchant__in=merchants)


class MerchantCheckoutListView(generics.ListAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        account = self.request.user
        merchants = account.merchant_set.all()
        merchant = get_object_or_404(merchants, id=self.kwargs['id'])
        return Checkout.objects.filter(merchant=merchant)

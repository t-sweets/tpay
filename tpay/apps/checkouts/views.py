from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Checkout
from .serializer import CheckoutSerializer
from common.permissions import IsMerchantOwnerOrReadOnly


class CheckoutView(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsMerchantOwnerOrReadOnly)
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

from rest_framework import permissions, generics

from .models import Checkout
from .serializer import CheckoutSerializer


class CheckoutView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

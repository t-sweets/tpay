from .serializer import TransactionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from deposits.models import Deposit
from checkouts.models import Checkout
from itertools import chain


class TransactionViewSet(viewsets.ViewSet):
    def get_marge_queryset(self):
        deposit_amount = Deposit.objects.all()
        checkout_amout = Checkout.objects.all()
        return sorted(chain(deposit_amount, checkout_amout), key=lambda instance: instance.created_time)

    def list(self, request):
        queryset = self.get_marge_queryset()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

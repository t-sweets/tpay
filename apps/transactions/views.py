from .serializer import TransactionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from deposits.models import Deposit
from checkouts.models import Checkout
from itertools import chain


class TransactionViewSet(viewsets.ViewSet):
    def get_marge_queryset(self, request):
        deposit = Deposit.objects.filter(user=request.user)
        checkout = Checkout.objects.filter(purchaser=request.user)
        return sorted(chain(deposit, checkout), key=lambda instance: instance.created_time)

    def list(self, request):
        queryset = self.get_marge_queryset(request)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

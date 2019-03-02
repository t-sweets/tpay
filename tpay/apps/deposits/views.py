from rest_framework import permissions, generics

from .models import Deposit
from .serializer import DepositSerializer


class DepositView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

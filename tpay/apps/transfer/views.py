from rest_framework import permissions, generics

from .models import Transfer
from .serializer import TransferSerializer


class TransferView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

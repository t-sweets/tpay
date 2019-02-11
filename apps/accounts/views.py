from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, mixins, viewsets
from rest_framework.response import Response

from .serializer import AccountSerializer, IdmSerializer
from .models import Account, Idm
from checkouts.models import Checkout
from checkouts.serializer import CheckoutSerializer


class AccountRegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=request.user.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        try:
            instance = self.queryset.get(pk=self.request.user.id)
            return instance
        except Account.DoesNotExist:
            raise Http404

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class IdmView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = IdmSerializer
    queryset = Idm.objects.all()


class AccountCheckoutViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             generics.GenericAPIView):
    serializer_class = CheckoutSerializer

    def get_queryset(self):
        purchaser = self.request.user
        return Checkout.objects.filter(purchaser=purchaser)

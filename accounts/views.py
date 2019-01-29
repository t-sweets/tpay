from rest_framework import permissions, generics
from rest_framework.response import Response
from django.db import transaction
from django.http import Http404

from rest_framework import status

from .serializer import AccountSerializer
from .models import User


class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = AccountSerializer


class AuthInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, format=None):
        return Response(data={
            'username': request.user.username,
            'display_name': request.user.balance,
            'email': request.user.email,
            'balance': request.user.balance,
        },
            status=status.HTTP_200_OK)


class AuthInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(pk=self.request.user.id)
            return instance
        except User.DoesNotExist:
            raise Http404


class AuthInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(pk=self.request.user.id)
            return instance
        except User.DoesNotExist:
            raise Http404

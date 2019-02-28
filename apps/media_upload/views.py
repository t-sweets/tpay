from rest_framework import permissions, generics

from .models import Image
from .serializer import ImageSerializer


class ImageView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

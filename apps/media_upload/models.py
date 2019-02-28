from django.db import models
import uuid
import os
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Image(BaseModel):
    def get_image_path(self, filename):
        prefix = 'images/'
        name = uuid.uuid4().hex
        extension = os.path.splitext(filename)[-1]
        return prefix + name + extension

    image = models.ImageField(
        upload_to=get_image_path,
        verbose_name=_('image'),
        height_field='height',
        width_field='width',
    )

    height = models.IntegerField(
        editable=False,
    )

    width = models.IntegerField(
        editable=False,
    )

from django.utils.translation import gettext_lazy as _
from django.db import models
import ulid


class ULIDField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 26
        super(ULIDField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(26)'


class BaseModel(models.Model):

    id = ULIDField(default=ulid.new, primary_key=True, unique=True, editable=False)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)
    deleted = models.BooleanField(_('deleted'), default=False)

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.deleted = True
        self.save()

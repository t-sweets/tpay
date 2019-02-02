from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid as uuid_lib

from accounts.models import Account


class Merchant(models.Model):
    uuid = models.UUIDField(default=uuid_lib.uuid4, unique=True, editable=False)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)
    name = models.CharField(_('merchant name'), max_length=30)
    accounts = models.ManyToManyField(Account)

    def __str__(self):
        return self.name

from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from accounts.models import Account


class Merchant(BaseModel):

    name = models.CharField(_('merchant name'), max_length=30)
    accounts = models.ManyToManyField(Account)
    is_active = models.BooleanField(_('is active'), default=True)

    def __str__(self):
        return self.name

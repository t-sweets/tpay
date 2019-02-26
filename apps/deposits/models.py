from django.db import models
from django.shortcuts import get_object_or_404

from common.models import BaseModel
from accounts.models import Account, Idm
from merchants.models import Merchant


class DepositManager(models.Manager):
    def deposit(self, request_data):

        try:
            user = Idm.objects.get(idm=request_data['idm']).account
        except Idm.DoesNotExist:
            raise ValueError(_('User auth failed'))

        deposit = self.model(
            amount=request_data['amount'],
            user=user,
        )
        Account.deposit(user.id, deposit.amount)
        deposit.save()


class Deposit(BaseModel):
    amount = models.IntegerField(_('amount'))
    merchant = models.ForeignKey(Merchant, on_delete=models.PROTECT)
    user = models.ForeignKey(Account, on_delete=models.PROTECT)

    objects = DepositManager()

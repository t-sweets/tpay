from django.db import models
from django.shortcuts import get_object_or_404

from common.models import BaseModel
from accounts.models import Account, Idm


class DepositManager(models.Manager):
    def deposit(self, request_data):
        user = get_object_or_404(Idm, idm=request_data['idm']).account
        deposit = self.model(
            amount=request_data['amount'],
            user=user,
        )
        Account.deposit(user.id, deposit.amount)
        deposit.save()


class Deposit(BaseModel):
    amount = models.IntegerField(_('amount'))
    user = models.ForeignKey(Account, on_delete=models.PROTECT)

    objects = DepositManager()

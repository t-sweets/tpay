from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from accounts.models import Account


class TransferManager(models.Manager):
    def transfer(self, request_data):

        transfer = self.model(
            user_from=request_data['user_from'],
            user_to=request_data['user_to'],
            amount=request_data['amount']
        )
        print(transfer)

        Account.withdraw(transfer.user_from.id, transfer.amount)
        Account.deposit(transfer.user_to.id, transfer.amount)
        transfer.save()

        return transfer


class Transfer(BaseModel):
    user_from = models.ForeignKey(Account,
                                  verbose_name=_('sender'),
                                  related_name='user_from',
                                  on_delete=models.PROTECT)
    user_to = models.ForeignKey(Account,
                                verbose_name=_('sender'),
                                related_name='user_to',
                                on_delete=models.PROTECT)
    amount = models.IntegerField(_('send value'))
    message = models.CharField(_('message'), max_length=255, blank=True, null=True)

    objects = TransferManager()

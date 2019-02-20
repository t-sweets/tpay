from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404

from common.models import BaseModel
from merchants.models import Merchant
from accounts.models import Account, Idm


class CheckoutManager(models.Manager):
    def checkout(self, request_data):

        try:
            purchaser = Idm.objects.get(idm=request_data['idm']).account
        except Idm.DoesNotExist:
            raise ValueError(_('User auth failed'))


        checkout = self.model(
            amount=request_data['amount'],
            payment_method=request_data['payment_method'],
            merchant=request_data['merchant'],
            purchaser=purchaser,
        )

        Account.withdraw(purchaser.id, checkout.amount)
        checkout.save()

        return checkout


class Checkout(BaseModel):
    CARD, QR = 0, 1
    PAYMENT_METHOD_CHOICES = (
        (CARD, 'FeliCa Card'),
        (QR, 'QR Code'),
    )

    amount = models.IntegerField(_('amount'))
    payment_method = models.IntegerField(_('payment method'), choices=PAYMENT_METHOD_CHOICES)
    merchant = models.ForeignKey(Merchant, on_delete=models.PROTECT)
    purchaser = models.ForeignKey(Account, on_delete=models.PROTECT)

    objects = CheckoutManager()

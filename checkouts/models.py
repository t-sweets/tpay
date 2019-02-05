from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid as uuid_lib
from django.shortcuts import get_object_or_404

from merchants.models import Merchant
from accounts.models import Account, Idm


class CheckoutManager(models.Manager):
    def checkout(self, request_data):

        purchaser = get_object_or_404(Idm, idm=request_data['idm']).account

        checkout = self.model(
            amount=request_data['amount'],
            payment_method=request_data['payment_method'],
            merchant=request_data['merchant'],
            purchaser=purchaser,
        )

        Account.withdraw(purchaser.id, checkout.amount)
        checkout.save()

        return checkout


class Checkout(models.Model):
    CARD, QR = 0, 1
    PAYMENT_METHOD_CHOICES = (
        (CARD, 'FeliCa Card'),
        (QR, 'QR Code'),
    )

    uuid = models.UUIDField(default=uuid_lib.uuid4, unique=True, editable=False)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)
    amount = models.IntegerField(_('amount'))
    payment_method = models.IntegerField(_('payment method'), choices=PAYMENT_METHOD_CHOICES)
    merchant = models.ForeignKey(Merchant, on_delete=models.PROTECT)
    purchaser = models.ForeignKey(Account, on_delete=models.PROTECT)

    objects = CheckoutManager()


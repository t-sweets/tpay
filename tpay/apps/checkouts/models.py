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

        purchaser = Account.withdraw(purchaser.id, request_data['amount'])

        checkout = self.model(
            amount=request_data['amount'],
            payment_method=request_data['payment_method'],
            merchant=request_data['merchant'],
            purchaser=purchaser,
        )

        checkout.save()

        return checkout

    def cancel(self, amount, payment_method, merchant, purchaser):
        cancel = self.model(
            amount=-amount,
            payment_method=payment_method,
            merchant=merchant,
            purchaser=purchaser,
        )
        cancel.save()
        return Account.deposit(purchaser.id, amount)


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
    type = 'checkout'

    objects = CheckoutManager()

    def delete(self, **kwargs):
        if self.deleted:
            raise ValueError(_('no content'))
        else:
            self.deleted = True
            self.purchaser = Checkout.objects.cancel(
                amount=self.amount,
                payment_method=self.payment_method,
                merchant=self.merchant,
                purchaser=self.purchaser,
            )
            self.save()

    def cash_value(self):
        return "{:,}".format(-self.amount)

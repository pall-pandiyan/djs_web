from django.db import models
from django.contrib.auth.models import User

from core import choices


class UserConfig(models.Model):
    """
    Model containing configuration unique to each user.

    Developer: Pall Pandiyan.S
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_level = models.IntegerField(choices=choices.SUBSCRIPTION_LEVEL_CHOICES, null=False, blank=False, default=0)


class SubscriptionConfig(models.Model):
    """
    Model containing details of subscription levels.
    
    Developer: Pall Pandiyan.S
    """
    subscription_level = models.IntegerField(choices=choices.SUBSCRIPTION_LEVEL_CHOICES, null=False, blank=False, unique=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.CharField(choices=choices.CURRENCY_CHOICES, default='INR', max_length=3, null=False, blank=False)

    class Meta:
        ordering = ['subscription_level']
        verbose_name = 'Subscription Configuration'
        verbose_name_plural = 'Subscription Configuration'

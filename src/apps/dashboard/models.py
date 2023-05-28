from django.db import models

from core.choices import SUBSCRIPTION_LEVEL_CHOICES


class DashboardMenu(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    order = models.IntegerField(unique=True, null=False, blank=False)
    url = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
    subscription_level = models.IntegerField(choices=SUBSCRIPTION_LEVEL_CHOICES, null=False, blank=False, default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Dashboard Menu'
        verbose_name_plural = 'Dashboard Menus'


class DashboardSubMenu(models.Model):
    menu = models.ForeignKey(DashboardMenu, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    order = models.IntegerField(unique=True, null=False, blank=False)
    url = models.CharField(max_length=50, unique=True, null=False, blank=False)
    subscription_level = models.IntegerField(choices=SUBSCRIPTION_LEVEL_CHOICES, null=False, blank=False, default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Dashboard Submenu'
        verbose_name_plural = 'Dashboard Submenus'


class ProfileMenu(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    order = models.IntegerField(unique=True, null=False, blank=False)
    url = models.CharField(max_length=50, unique=True, null=False, blank=False)
    subscription_level = models.IntegerField(choices=SUBSCRIPTION_LEVEL_CHOICES, null=False, blank=False, default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Profile Menu'
        verbose_name_plural = 'Profile Menus'

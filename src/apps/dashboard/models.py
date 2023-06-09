from django.db import models

from core.choices import SUBSCRIPTION_LEVEL_CHOICES


class DashboardMenu(models.Model):
    """
    Model containing dashboard menus, we are using a table to dynamically change the dashboard items.

    Developer: Pall Pandiyan.S
    """
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    order = models.IntegerField(unique=True, null=False, blank=False)
    url = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
    subscription_level = models.IntegerField(choices=SUBSCRIPTION_LEVEL_CHOICES, null=False, blank=False, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Dashboard Menu'
        verbose_name_plural = 'Dashboard Menus'


class DashboardSubMenu(models.Model):
    """
    Model containing submenus of DashboardMenu, we are using a table to dynamically change the dashboard items.
    
    Developer: Pall Pandiyan.S
    """
    menu = models.ForeignKey(DashboardMenu, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    order = models.IntegerField(unique=True, null=False, blank=False)
    url = models.CharField(max_length=50, unique=True, null=False, blank=False)
    subscription_level = models.IntegerField(choices=SUBSCRIPTION_LEVEL_CHOICES, null=False, blank=False, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Dashboard Submenu'
        verbose_name_plural = 'Dashboard Submenus'


class ProfileMenu(models.Model):
    """
    Model containing profile menus, we are using a table to dynamically change the profile items.
    
    Developer: Pall Pandiyan.S
    """
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    order = models.IntegerField(unique=True, null=False, blank=False)
    url = models.CharField(max_length=50, unique=True, null=False, blank=False)
    subscription_level = models.IntegerField(choices=SUBSCRIPTION_LEVEL_CHOICES, null=False, blank=False, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Profile Menu'
        verbose_name_plural = 'Profile Menus'

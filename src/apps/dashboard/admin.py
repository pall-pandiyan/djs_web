from django.contrib import admin

from . import models


admin.site.register(models.ProfileMenu)
admin.site.register(models.DashboardMenu)
admin.site.register(models.DashboardSubMenu)

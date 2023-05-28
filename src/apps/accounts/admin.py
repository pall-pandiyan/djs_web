from django.contrib import admin
from . import models


admin.site.register(models.UserConfig)
admin.site.register(models.SubscriptionConfig)

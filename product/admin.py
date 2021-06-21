from django.contrib import admin
from . import models

admin.site.register(models.Game)
admin.site.register(models.Item)
admin.site.register(models.Comment)
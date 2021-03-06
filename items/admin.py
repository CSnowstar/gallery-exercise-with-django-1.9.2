# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Photo)
admin.site.register(Item, ItemAdmin)

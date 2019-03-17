# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    search_fields = ('message', 'extra_tags')
    list_display = ('message', 'extra_tags',
                    'level', 'is_active',
                    'crdate', 'tstamp')
    list_filter = ('level', 'is_active',
                   'crdate', 'tstamp')
    #date_hierarchy = 'crdate'

admin.site.register(Announcement, AnnouncementAdmin)

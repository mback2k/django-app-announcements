# -*- coding: utf-8 -*-
from django.conf import settings
from .models import Announcement

def announcements(request):
    announcements = Announcement.objects.filter(is_active=True)

    template_values = {
        'announcements': announcements,
    }

    return template_values

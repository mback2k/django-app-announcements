# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.messages import constants, utils
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

LEVEL_TAGS = utils.get_level_tags()

class Announcement(models.Model):
    message = models.TextField(_('Message'))
    level = models.SmallIntegerField(_('Level'), choices=LEVEL_TAGS.items())
    extra_tags = models.TextField(_('Extra tags'), blank=True)
    is_active = models.BooleanField(_('Is active'), default=True)

    crdate = models.DateTimeField(_('Date created'), auto_now_add=True)
    tstamp = models.DateTimeField(_('Date changed'), auto_now=True)

    class Meta:
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')
        ordering = ('-level', '-crdate', '-tstamp')

    def __str__(self):
        return force_text(self.message)

    def _get_tags(self):
        extra_tags = force_text(self.extra_tags, strings_only=True)
        if extra_tags and self.level_tag:
            return ' '.join([extra_tags, self.level_tag])
        elif extra_tags:
            return extra_tags
        elif self.level_tag:
            return self.level_tag
        return ''
    tags = property(_get_tags)

    @property
    def level_tag(self):
        return force_text(LEVEL_TAGS.get(self.level, ''), strings_only=True)

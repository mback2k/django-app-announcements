# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(verbose_name='Message')),
                ('level', models.SmallIntegerField(verbose_name='Level', choices=[(40, b'error'), (25, b'success'), (10, b'debug'), (20, b'info'), (30, b'warning')])),
                ('extra_tags', models.TextField(default='', verbose_name='Extra tags')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('tstamp', models.DateTimeField(auto_now=True, verbose_name='Date changed')),
            ],
            options={
                'ordering': ('-level', '-crdate', '-tstamp'),
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
            },
            bases=(models.Model,),
        ),
    ]

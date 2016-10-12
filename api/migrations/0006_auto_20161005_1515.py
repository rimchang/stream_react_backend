# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_userprofile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age_range',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age_range_max',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age_range_min',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

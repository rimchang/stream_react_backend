# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161005_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='user_id',
            field=models.ForeignKey(related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]

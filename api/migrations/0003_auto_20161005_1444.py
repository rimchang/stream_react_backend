# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_userprofile_f_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='user_id',
            field=models.ForeignKey(related_name='upload_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

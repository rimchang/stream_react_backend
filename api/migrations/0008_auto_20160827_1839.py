# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160827_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='upload_id',
            field=models.ForeignKey(related_name='comments', blank=True, to='api.Upload', null=True),
        ),
    ]

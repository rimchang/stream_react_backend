# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160817_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]

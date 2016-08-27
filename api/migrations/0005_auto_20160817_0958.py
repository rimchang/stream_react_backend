# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20160817_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('follower_id', models.ForeignKey(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(related_name='friends', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='follower',
            name='follower_id',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('user_id', 'follower_id')]),
        ),
    ]

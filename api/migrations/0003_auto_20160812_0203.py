# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20160812_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('follower_id', models.ForeignKey(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(related_name='friends', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Searche',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(upload_to=b'original/%Y/%m/%d')),
                ('caption', models.TextField(max_length=500, blank=True)),
                ('location', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='upload_id',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user_id',
        ),
        migrations.AlterUniqueTogether(
            name='followers',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='followers',
            name='follower_id',
        ),
        migrations.RemoveField(
            model_name='followers',
            name='user_id',
        ),
        migrations.AlterUniqueTogether(
            name='likes',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='likes',
            name='upload_id',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='searches',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='uploads',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.DeleteModel(
            name='Searches',
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
        migrations.AddField(
            model_name='like',
            name='upload_id',
            field=models.ForeignKey(blank=True, to='api.Upload', null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='upload_id',
            field=models.ForeignKey(blank=True, to='api.Upload', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user_id', 'upload_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together=set([('user_id', 'follower_id')]),
        ),
    ]

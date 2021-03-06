# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('key', models.CharField(db_index=True, max_length=64)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('place', models.CharField(max_length=256)),
                ('book_start', models.DateTimeField(db_index=True)),
                ('book_end', models.DateTimeField(db_index=True)),
                ('total_tickets', models.IntegerField()),
                ('status', models.IntegerField()),
                ('pic_url', models.CharField(max_length=256)),
                ('remain_tickets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(db_index=True, max_length=32)),
                ('unique_id', models.CharField(db_index=True, max_length=64, unique=True)),
                ('status', models.IntegerField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wechat.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_id', models.CharField(db_index=True, max_length=64, unique=True)),
                ('student_id', models.CharField(blank=True, db_index=True, max_length=32, null=True, unique=True)),
            ],
        ),
    ]

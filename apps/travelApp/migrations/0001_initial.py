# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('trDateFrom', models.DateField()),
                ('trDateTo', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_plans', to='loginApp.User')),
                ('users', models.ManyToManyField(related_name='plans', to='loginApp.User')),
            ],
        ),
    ]

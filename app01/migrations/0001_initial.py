# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-07-02 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App01Cities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=10, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='App01Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updateDate', models.DateField()),
                ('diagnosis', models.IntegerField()),
                ('cure', models.IntegerField()),
                ('dead', models.IntegerField()),
                ('new_diagnosis', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.App01Cities')),
            ],
            options={
                'db_table': 'city_detail',
            },
        ),
        migrations.CreateModel(
            name='App01News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=25, null=True)),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]

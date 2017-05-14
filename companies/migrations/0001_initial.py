# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('materials', models.ManyToManyField(related_name='companies', to='materials.Materials')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('volume', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='companies',
            name='prices',
            field=models.ManyToManyField(related_name='companies', to='companies.Price'),
        ),
    ]
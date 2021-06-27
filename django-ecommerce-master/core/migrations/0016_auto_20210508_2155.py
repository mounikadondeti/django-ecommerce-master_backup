# Generated by Django 2.2.14 on 2021-05-08 16:25

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210506_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=100, verbose_name=core.models.Category),
        ),
    ]

# Generated by Django 2.2.14 on 2021-05-06 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210505_0736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='value',
        ),
    ]

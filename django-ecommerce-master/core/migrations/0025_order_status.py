# Generated by Django 2.2.14 on 2021-05-23 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]

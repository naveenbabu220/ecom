# Generated by Django 3.1.4 on 2021-02-25 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210225_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='startdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 3.1.1 on 2022-08-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kendaraan', '0005_auto_20220807_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='kendaraan',
            name='keterangan',
            field=models.TextField(blank=True, null=True),
        ),
    ]

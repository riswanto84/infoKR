# Generated by Django 3.1.1 on 2022-08-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kendaraan', '0004_kendaraan_merk_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='alamat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pegawai',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

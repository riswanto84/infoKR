# Generated by Django 3.1.1 on 2022-08-07 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kendaraan', '0002_pegawai_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='foto',
            field=models.ImageField(blank=True, default='profilepics/avatar.jpg', null=True, upload_to='foto_pegawai'),
        ),
    ]

# Generated by Django 3.1.1 on 2022-08-18 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kendaraan', '0007_auto_20220818_0707'),
        ('account', '0004_auto_20220818_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='useradmin',
            name='nip',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='useradmin',
            name='unit_kerja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kendaraan.unitkerja'),
        ),
    ]

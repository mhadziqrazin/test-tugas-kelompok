# Generated by Django 4.1.2 on 2022-10-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donasi', '0002_donasi_terkumpul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donasi',
            name='foto',
            field=models.ImageField(upload_to='foto/'),
        ),
    ]
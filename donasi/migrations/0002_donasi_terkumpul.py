# Generated by Django 4.1.2 on 2022-10-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donasi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="donasi",
            name="terkumpul",
            field=models.BigIntegerField(default=0),
        ),
    ]
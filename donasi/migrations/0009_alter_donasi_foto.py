# Generated by Django 4.1.2 on 2022-10-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donasi", "0008_mendonasikan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donasi", name="foto", field=models.ImageField(upload_to=""),
        ),
    ]

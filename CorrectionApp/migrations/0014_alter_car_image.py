# Generated by Django 3.2.3 on 2021-05-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CorrectionApp', '0013_rename_postimage_carimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.FileField(blank=True, upload_to='car_images'),
        ),
    ]

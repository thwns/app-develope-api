# Generated by Django 3.2.13 on 2022-06-21 12:19

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220608_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.date_image_file_path),
        ),
    ]
# Generated by Django 3.2 on 2022-05-23 20:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookcase', '0006_auto_20220523_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='rack_id',
            field=models.UUIDField(default=uuid.UUID('8a052ce9-c00d-46b7-ae32-58108801cbc6')),
        ),
    ]
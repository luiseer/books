# Generated by Django 3.2 on 2022-05-24 02:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookcase', '0011_auto_20220524_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='rack_id',
            field=models.UUIDField(default=uuid.UUID('0ebc0164-fe09-4cbd-9bc0-a3b242fd07c1')),
        ),
    ]

# Generated by Django 3.2 on 2022-05-23 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0004_alter_book_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.UUIDField(default=uuid.UUID('166bbd38-9570-4950-a3d4-269dc7ca52a2')),
        ),
    ]
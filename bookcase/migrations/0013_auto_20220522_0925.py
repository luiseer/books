# Generated by Django 3.2 on 2022-05-22 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_alter_book_book_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookcase', '0012_auto_20220522_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rack',
            name='rack_id',
            field=models.UUIDField(default=uuid.UUID('5adcf7d9-f7c0-4d2e-b4d0-ec6a5b925334')),
        ),
    ]
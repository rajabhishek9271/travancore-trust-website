# Generated by Django 3.0.6 on 2020-11-06 11:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trust', '0006_auto_20201106_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousdonation',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regulardonation',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

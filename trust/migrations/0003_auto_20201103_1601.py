# Generated by Django 3.1 on 2020-11-03 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trust', '0002_auto_20201102_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anonymousdonation',
            old_name='donation_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='regulardonation',
            old_name='donation_type',
            new_name='type',
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-24 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='phone',
            new_name='description',
        ),
    ]
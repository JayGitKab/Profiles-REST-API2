# Generated by Django 2.2 on 2020-04-24 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20200421_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='user_profiles',
            new_name='user_profile',
        ),
    ]

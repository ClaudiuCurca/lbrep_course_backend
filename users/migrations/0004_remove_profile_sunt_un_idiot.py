# Generated by Django 4.1.2 on 2022-11-07 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_sunt_un_idiot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='sunt_un_idiot',
        ),
    ]
# Generated by Django 3.2.20 on 2023-09-04 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_rename_friends_friends_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='friends',
            new_name='message_friends',
        ),
    ]

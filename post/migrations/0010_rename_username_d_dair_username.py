# Generated by Django 3.2.20 on 2023-10-01 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_dair_username_d'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dair',
            old_name='username_d',
            new_name='username',
        ),
    ]

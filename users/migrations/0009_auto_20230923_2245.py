# Generated by Django 3.2.20 on 2023-09-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='profile_picture/default.png', upload_to='profile_picture/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture_background',
            field=models.ImageField(default='profile_picture_background/default.jpeg', upload_to='profile_picture_background/'),
        ),
    ]
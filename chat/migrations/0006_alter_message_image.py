# Generated by Django 3.2.19 on 2023-08-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(default='pgb.png', null=True, upload_to='images/'),
        ),
    ]

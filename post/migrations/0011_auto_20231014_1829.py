# Generated by Django 3.2.20 on 2023-10-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_rename_username_d_dair_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dair',
            name='dair_img',
        ),
        migrations.RemoveField(
            model_name='dair',
            name='dair_video',
        ),
        migrations.AddField(
            model_name='dair',
            name='dair_created_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]

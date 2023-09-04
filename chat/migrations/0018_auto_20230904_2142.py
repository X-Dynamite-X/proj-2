# Generated by Django 3.2.20 on 2023-09-04 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0017_auto_20230904_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message_friends',
        ),
        migrations.AlterField(
            model_name='message',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(default='pgb.png', null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]
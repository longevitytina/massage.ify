# Generated by Django 3.0.5 on 2020-05-05 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200504_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlisttechnique',
            name='time',
        ),
        migrations.AddField(
            model_name='playlisttechnique',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='image_url',
            field=models.URLField(default='https://source.unsplash.com/random/30x50'),
        ),
    ]
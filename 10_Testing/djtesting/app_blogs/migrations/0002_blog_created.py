# Generated by Django 4.1.5 on 2023-02-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='1990-05-31 00:00'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2 on 2023-01-05 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0010_advertisements_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisements',
            old_name='numberViews',
            new_name='number_views',
        ),
    ]
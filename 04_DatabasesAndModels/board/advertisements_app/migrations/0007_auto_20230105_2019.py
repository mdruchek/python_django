# Generated by Django 2.2 on 2023-01-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0006_auto_20230105_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='publication_end_date',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]

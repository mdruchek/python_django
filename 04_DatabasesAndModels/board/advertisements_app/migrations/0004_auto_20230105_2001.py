# Generated by Django 2.2 on 2023-01-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0003_auto_20230105_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='publication_end_date',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]

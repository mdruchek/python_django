# Generated by Django 4.1.5 on 2023-01-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0011_auto_20230105_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='publication_end_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]

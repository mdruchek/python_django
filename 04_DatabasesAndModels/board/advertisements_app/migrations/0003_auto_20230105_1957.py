# Generated by Django 2.2 on 2023-01-05 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0002_auto_20230105_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementcategory',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisements_app.AdvertisementAuthor', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisements_app.AdvertisementCategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='advertisements',
            name='publication_end_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]

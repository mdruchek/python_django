# Generated by Django 4.1.5 on 2023-04-06 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0007_alter_stocks_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop_app.product', verbose_name='Продукт'),
        ),
    ]
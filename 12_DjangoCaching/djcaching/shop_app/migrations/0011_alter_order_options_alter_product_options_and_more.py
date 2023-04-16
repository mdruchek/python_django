# Generated by Django 4.1.5 on 2023-04-08 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0010_alter_offer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='stocks',
            options={'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
    ]
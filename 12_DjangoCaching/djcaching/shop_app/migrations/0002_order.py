# Generated by Django 4.1.5 on 2023-04-04 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.userprofile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
            },
        ),
    ]

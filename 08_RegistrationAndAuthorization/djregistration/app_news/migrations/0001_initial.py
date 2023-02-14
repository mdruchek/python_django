# Generated by Django 4.1.5 on 2023-01-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_created=True)),
                ('user', models.CharField(max_length=20, verbose_name='Пользователь')),
                ('content', models.TextField(max_length=200, verbose_name='Содержание')),
            ],
        ),
    ]
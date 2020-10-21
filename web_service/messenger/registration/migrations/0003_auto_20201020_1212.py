# Generated by Django 3.1.2 on 2020-10-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_information_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='gender',
            field=models.CharField(default='1', max_length=2, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='information',
            name='age',
            field=models.CharField(default='1', max_length=2, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='information',
            name='color',
            field=models.CharField(default='1', max_length=20, verbose_name='Любимый цвет'),
        ),
    ]

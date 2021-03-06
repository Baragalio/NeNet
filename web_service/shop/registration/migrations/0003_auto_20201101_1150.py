# Generated by Django 3.1.2 on 2020-11-01 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0002_auto_20201023_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='information',
            name='color',
            field=models.IntegerField(default=0, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='information',
            name='count_fr',
            field=models.IntegerField(default=0, verbose_name='Count_friends'),
        ),
        migrations.AlterField(
            model_name='information',
            name='gender',
            field=models.IntegerField(default=0, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='information',
            name='purpose',
            field=models.IntegerField(default=0, verbose_name='Purpose'),
        ),
        migrations.AlterField(
            model_name='information',
            name='scope',
            field=models.IntegerField(default=0, verbose_name='Scope'),
        ),
        migrations.AlterField(
            model_name='information',
            name='season',
            field=models.IntegerField(default=0, verbose_name='Season'),
        ),
        migrations.AlterField(
            model_name='information',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='information', to=settings.AUTH_USER_MODEL),
        ),
    ]

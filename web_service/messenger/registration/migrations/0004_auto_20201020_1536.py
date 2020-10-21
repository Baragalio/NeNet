# Generated by Django 3.1.2 on 2020-10-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20201020_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='choice1',
            field=models.CharField(default='1', max_length=2, verbose_name='Choice1'),
        ),
        migrations.AddField(
            model_name='information',
            name='count_fr',
            field=models.CharField(default='1', max_length=2, verbose_name='Count_friends'),
        ),
        migrations.AddField(
            model_name='information',
            name='pref',
            field=models.CharField(default='1', max_length=2, verbose_name='Preference'),
        ),
        migrations.AddField(
            model_name='information',
            name='pref2',
            field=models.CharField(default='1', max_length=6, verbose_name='Preference_menu'),
        ),
        migrations.AddField(
            model_name='information',
            name='purpose',
            field=models.CharField(default='1', max_length=2, verbose_name='Purpose'),
        ),
        migrations.AddField(
            model_name='information',
            name='season',
            field=models.CharField(default='1', max_length=2, verbose_name='Season'),
        ),
        migrations.AddField(
            model_name='information',
            name='sсope',
            field=models.CharField(default='1', max_length=2, verbose_name='Scope'),
        ),
        migrations.AddField(
            model_name='information',
            name='theme',
            field=models.CharField(default='1', max_length=2, verbose_name='Theme'),
        ),
        migrations.AlterField(
            model_name='information',
            name='age',
            field=models.CharField(default='1', max_length=2, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='information',
            name='color',
            field=models.CharField(default='1', max_length=20, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='information',
            name='gender',
            field=models.CharField(default='1', max_length=2, verbose_name='Gender'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-01 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.IntegerField(default=0, verbose_name='choice1')),
                ('choice2', models.IntegerField(default=0, verbose_name='choice2')),
                ('choice3', models.IntegerField(default=0, verbose_name='choice3')),
                ('choice4', models.IntegerField(default=0, verbose_name='choice4')),
                ('choice5', models.IntegerField(default=0, verbose_name='choice5')),
                ('theme', models.IntegerField(default=0, verbose_name='theme')),
                ('pref', models.IntegerField(default=0, verbose_name='pref')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='more_information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

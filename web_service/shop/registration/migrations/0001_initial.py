# Generated by Django 3.1.2 on 2020-10-23 13:39

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
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.IntegerField(default=1, verbose_name='Color')),
                ('age', models.IntegerField(default=1, verbose_name='Age')),
                ('gender', models.IntegerField(default=1, verbose_name='Gender')),
                ('season', models.IntegerField(default=1, verbose_name='Season')),
                ('sсope', models.IntegerField(default=1, verbose_name='Scope')),
                ('purpose', models.IntegerField(default=1, verbose_name='Purpose')),
                ('count_fr', models.IntegerField(default=1, verbose_name='Count_friends')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
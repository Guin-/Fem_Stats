# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('sleep', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('alcohol_intake', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('exercise', models.CharField(blank=True, max_length=10, choices=[(b'less than 30', b'<30'), (b'half hour to hour', b'30-60'), (b'60+', b'60+')])),
                ('stress_level', models.CharField(blank=True, max_length=6, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'High', b'High')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='mental',
            name='user',
        ),
        migrations.RemoveField(
            model_name='physical',
            name='user',
        ),
        migrations.DeleteModel(
            name='Mental',
        ),
        migrations.DeleteModel(
            name='Physical',
        ),
    ]

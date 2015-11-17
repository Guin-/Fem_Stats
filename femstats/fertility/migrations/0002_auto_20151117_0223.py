# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fertility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasalBodyTemp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('time', models.TimeField(verbose_name=b'Time')),
                ('temperature', models.PositiveSmallIntegerField()),
                ('scale', models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Fahrenheit'), (b'C', b'Celsius')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BasalBodyTemperature',
        ),
        migrations.AddField(
            model_name='cervical',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date'),
        ),
        migrations.AddField(
            model_name='cervical',
            name='mucus',
            field=models.CharField(default=b'D', max_length=10, choices=[(b'D', b'Dry'), (b'S', b'Sticky'), (b'C', b'Creamy'), (b'W', b'Watery'), (b'EW', b'Egg White')]),
        ),
        migrations.AddField(
            model_name='cervical',
            name='opening',
            field=models.CharField(default=b'Open', max_length=10, choices=[(b'Open', b'Open'), (b'MD', b'Medium'), (b'Closed', b'Closed')]),
        ),
        migrations.AddField(
            model_name='cervical',
            name='position',
            field=models.CharField(default=b'HI', max_length=10, choices=[(b'LW', b'Low'), (b'MD', b'Medium'), (b'HI', b'High')]),
        ),
        migrations.AddField(
            model_name='cervical',
            name='texture',
            field=models.CharField(default=b'FM', max_length=10, choices=[(b'ST', b'Soft'), (b'MD', b'Medium'), (b'FM', b'Firm')]),
        ),
        migrations.AddField(
            model_name='cervical',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='period',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date'),
        ),
        migrations.AddField(
            model_name='period',
            name='flow',
            field=models.CharField(default=b'SP', max_length=10, choices=[(b'SP', b'Spotting'), (b'L', b'Light'), (b'M', b'Medium'), (b'H', b'Heavy')]),
        ),
        migrations.AddField(
            model_name='period',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

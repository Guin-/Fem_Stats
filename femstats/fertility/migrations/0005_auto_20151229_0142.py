# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fertility', '0004_auto_20151216_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name=b'Time')),
                ('temperature', models.DecimalField(max_digits=6, decimal_places=2)),
                ('scale', models.CharField(max_length=1, choices=[(b'F', b'Fahrenheit'), (b'C', b'Celsius')])),
                ('mucus', models.CharField(max_length=10, choices=[(b'D', b'Dry'), (b'S', b'Sticky'), (b'C', b'Creamy'), (b'W', b'Watery'), (b'EW', b'Egg White')])),
                ('position', models.CharField(max_length=10, choices=[(b'LW', b'Low'), (b'MD', b'Medium'), (b'HI', b'High')])),
                ('texture', models.CharField(max_length=10, choices=[(b'ST', b'Soft'), (b'MD', b'Medium'), (b'FM', b'Firm')])),
                ('opening', models.CharField(max_length=10, choices=[(b'Open', b'Open'), (b'MD', b'Medium'), (b'Closed', b'Closed')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='basalbodytemp',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cervical',
            name='user',
        ),
        migrations.DeleteModel(
            name='BasalBodyTemp',
        ),
        migrations.DeleteModel(
            name='Cervical',
        ),
    ]

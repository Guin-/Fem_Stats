# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fertility', '0003_auto_20151204_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basalbodytemp',
            name='temperature',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='basalbodytemp',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=b'Time'),
        ),
    ]

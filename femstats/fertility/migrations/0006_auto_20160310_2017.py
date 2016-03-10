# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fertility', '0005_auto_20151229_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertility',
            name='mucus',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Dry', b'Dry'), (b'Sticky', b'Sticky'), (b'Creamy', b'Creamy'), (b'Watery', b'Watery'), (b'Egg White', b'Egg White')]),
        ),
        migrations.AlterField(
            model_name='fertility',
            name='opening',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Open', b'Open'), (b'Medium', b'Medium'), (b'Closed', b'Closed')]),
        ),
        migrations.AlterField(
            model_name='fertility',
            name='position',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'High', b'High')]),
        ),
        migrations.AlterField(
            model_name='fertility',
            name='scale',
            field=models.CharField(blank=True, max_length=1, choices=[(b'F', b'Fahrenheit'), (b'C', b'Celsius')]),
        ),
        migrations.AlterField(
            model_name='fertility',
            name='temperature',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='fertility',
            name='texture',
            field=models.CharField(blank=True, max_length=10, choices=[(b'Soft', b'Soft'), (b'Medium', b'Medium'), (b'Firm', b'Firm')]),
        ),
        migrations.AlterField(
            model_name='period',
            name='flow',
            field=models.CharField(max_length=10, choices=[(b'Spotting', b'Spotting'), (b'Light', b'Light'), (b'Medium', b'Medium'), (b'Heavy', b'Heavy')]),
        ),
    ]

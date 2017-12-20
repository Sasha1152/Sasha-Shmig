# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0006_auto_20171220_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moon',
            options={'ordering': ['number'], 'verbose_name': 'moon', 'verbose_name_plural': 'moons'},
        ),
        migrations.AlterModelOptions(
            name='planet',
            options={'ordering': ['number'], 'verbose_name': 'planet', 'verbose_name_plural': 'planets'},
        ),
        migrations.AlterField(
            model_name='moon',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='moon',
            name='number',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='planet',
            name='planet_mass_to_earth',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, verbose_name='Planet mass relative to an Earth'),
        ),
    ]

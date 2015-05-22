# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelMacro', '0002_auto_20150520_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='sect_var',
            field=models.ForeignKey(db_column=b'id_Secteur', blank=True, to='ModelMacro.Secteur', null=True),
        ),
    ]

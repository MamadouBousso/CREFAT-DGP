# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelMacro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variable',
            old_name='type',
            new_name='typeVariable',
        ),
    ]

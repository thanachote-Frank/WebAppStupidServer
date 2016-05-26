# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='input',
            new_name='inputText',
        ),
    ]

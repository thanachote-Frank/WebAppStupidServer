# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop', '0002_auto_20160527_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='inputText',
            new_name='input',
        ),
    ]

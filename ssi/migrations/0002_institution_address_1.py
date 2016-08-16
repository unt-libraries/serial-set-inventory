# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='address_1',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_input',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='user_input',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='snippets',
            field=models.ManyToManyField(to='service.Snippet', db_table=b'service_snippet'),
        ),
    ]

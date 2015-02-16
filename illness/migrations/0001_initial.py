# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Illness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('name_en', models.CharField(max_length=1000, null=True)),
                ('name_sr', models.CharField(max_length=1000, null=True)),
                ('slug', models.SlugField()),
                ('slug_en', models.SlugField(null=True)),
                ('slug_sr', models.SlugField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Illnesses',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name': 'stage',
                'verbose_name_plural': 'stages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StageTransition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.ForeignKey(related_name='outbound_transitions', verbose_name=b'source stage', to='dc_workflows.Stage')),
                ('target', models.ForeignKey(related_name='inbound_transitions', verbose_name=b'target stage', to='dc_workflows.Stage')),
            ],
            options={
                'verbose_name': 'stage transition',
                'verbose_name_plural': 'stage transitions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nombre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stage',
            name='workflow',
            field=models.ForeignKey(related_name='stages', to='dc_workflows.Workflow'),
            preserve_default=True,
        ),
    ]

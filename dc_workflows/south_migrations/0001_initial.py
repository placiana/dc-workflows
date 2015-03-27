# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workflow'
        db.create_table(u'dc_workflows_workflow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dc_workflows', ['Workflow'])

        # Adding model 'Stage'
        db.create_table(u'dc_workflows_stage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stages', to=orm['dc_workflows.Workflow'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dc_workflows', ['Stage'])

        # Adding model 'StageTransition'
        db.create_table(u'dc_workflows_stagetransition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='outbound_transitions', to=orm['dc_workflows.Stage'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inbound_transitions', to=orm['dc_workflows.Stage'])),
        ))
        db.send_create_signal(u'dc_workflows', ['StageTransition'])


    def backwards(self, orm):
        # Deleting model 'Workflow'
        db.delete_table(u'dc_workflows_workflow')

        # Deleting model 'Stage'
        db.delete_table(u'dc_workflows_stage')

        # Deleting model 'StageTransition'
        db.delete_table(u'dc_workflows_stagetransition')


    models = {
        u'dc_workflows.stage': {
            'Meta': {'object_name': 'Stage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stages'", 'to': u"orm['dc_workflows.Workflow']"})
        },
        u'dc_workflows.stagetransition': {
            'Meta': {'object_name': 'StageTransition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outbound_transitions'", 'to': u"orm['dc_workflows.Stage']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inbound_transitions'", 'to': u"orm['dc_workflows.Stage']"})
        },
        u'dc_workflows.workflow': {
            'Meta': {'object_name': 'Workflow'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dc_workflows']
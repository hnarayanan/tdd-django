# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'List'
        db.create_table(u'lists_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'lists', ['List'])

        # Adding model 'Item'
        db.create_table(u'lists_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lists.List'])),
        ))
        db.send_create_signal(u'lists', ['Item'])

        # Adding unique constraint on 'Item', fields ['list', 'text']
        db.create_unique(u'lists_item', ['list_id', 'text'])


    def backwards(self, orm):
        # Removing unique constraint on 'Item', fields ['list', 'text']
        db.delete_unique(u'lists_item', ['list_id', 'text'])

        # Deleting model 'List'
        db.delete_table(u'lists_list')

        # Deleting model 'Item'
        db.delete_table(u'lists_item')


    models = {
        u'lists.item': {
            'Meta': {'ordering': "('id',)", 'unique_together': "(('list', 'text'),)", 'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lists.List']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'lists.list': {
            'Meta': {'object_name': 'List'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['lists']
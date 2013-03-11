# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table('pickup_finder_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('normalized_location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data_source', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('touch_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated_datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('pickup_finder', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table('pickup_finder_game')


    models = {
        'pickup_finder.game': {
            'Meta': {'object_name': 'Game'},
            'data_source': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'normalized_location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'touch_datetime': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['pickup_finder']
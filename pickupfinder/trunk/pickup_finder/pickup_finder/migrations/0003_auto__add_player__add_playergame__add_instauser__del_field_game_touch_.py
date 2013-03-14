# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table('pickup_finder_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('pickup_finder', ['Player'])

        # Adding model 'PlayerGame'
        db.create_table('pickup_finder_playergame', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pickup_finder.Player'])),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pickup_finder.Game'])),
            ('chance_attending', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('pickup_finder', ['PlayerGame'])

        # Adding model 'InstaUser'
        db.create_table('pickup_finder_instauser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('pickup_finder', ['InstaUser'])

        # Deleting field 'Game.touch_datetime'
        db.delete_column('pickup_finder_game', 'touch_datetime')

        # Deleting field 'Game.last_updated_datetime'
        db.delete_column('pickup_finder_game', 'last_updated_datetime')

        # Deleting field 'Game.data_source'
        db.delete_column('pickup_finder_game', 'data_source')

        # Adding field 'Game.creator'
        db.add_column('pickup_finder_game', 'creator',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['pickup_finder.InstaUser']),
                      keep_default=False)

        # Adding field 'Game.public'
        db.add_column('pickup_finder_game', 'public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Game.person_cap'
        db.add_column('pickup_finder_game', 'person_cap',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Game.created'
        db.add_column('pickup_finder_game', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Adding field 'Game.modified'
        db.add_column('pickup_finder_game', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Adding field 'Game.starts_at'
        db.add_column('pickup_finder_game', 'starts_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table('pickup_finder_player')

        # Deleting model 'PlayerGame'
        db.delete_table('pickup_finder_playergame')

        # Deleting model 'InstaUser'
        db.delete_table('pickup_finder_instauser')

        # Adding field 'Game.touch_datetime'
        db.add_column('pickup_finder_game', 'touch_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Adding field 'Game.last_updated_datetime'
        db.add_column('pickup_finder_game', 'last_updated_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Adding field 'Game.data_source'
        db.add_column('pickup_finder_game', 'data_source',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1),
                      keep_default=False)

        # Deleting field 'Game.creator'
        db.delete_column('pickup_finder_game', 'creator_id')

        # Deleting field 'Game.public'
        db.delete_column('pickup_finder_game', 'public')

        # Deleting field 'Game.person_cap'
        db.delete_column('pickup_finder_game', 'person_cap')

        # Deleting field 'Game.created'
        db.delete_column('pickup_finder_game', 'created')

        # Deleting field 'Game.modified'
        db.delete_column('pickup_finder_game', 'modified')

        # Deleting field 'Game.starts_at'
        db.delete_column('pickup_finder_game', 'starts_at')


    models = {
        'pickup_finder.game': {
            'Meta': {'object_name': 'Game'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pickup_finder.InstaUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'normalized_location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'person_cap': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'starts_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        'pickup_finder.instauser': {
            'Meta': {'object_name': 'InstaUser'},
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pickup_finder.player': {
            'Meta': {'object_name': 'Player'},
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pickup_finder.playergame': {
            'Meta': {'object_name': 'PlayerGame'},
            'chance_attending': ('django.db.models.fields.SmallIntegerField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pickup_finder.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pickup_finder.Player']"})
        }
    }

    complete_apps = ['pickup_finder']
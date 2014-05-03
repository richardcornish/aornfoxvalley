# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Member.office'
        db.delete_column('members_member', 'office_id')

        # Adding M2M table for field offices on 'Member'
        db.create_table('members_member_offices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm['members.member'], null=False)),
            ('office', models.ForeignKey(orm['members.office'], null=False))
        ))
        db.create_unique('members_member_offices', ['member_id', 'office_id'])


    def backwards(self, orm):
        # Adding field 'Member.office'
        db.add_column('members_member', 'office',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Office'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field offices on 'Member'
        db.delete_table('members_member_offices')


    models = {
        'members.committee': {
            'Meta': {'ordering': "['title']", 'object_name': 'Committee'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'members.member': {
            'Meta': {'ordering': "['-last_name', 'first_name']", 'object_name': 'Member'},
            'committees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['members.Committee']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'offices': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['members.Office']", 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'members.office': {
            'Meta': {'ordering': "['title']", 'object_name': 'Office'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['members']
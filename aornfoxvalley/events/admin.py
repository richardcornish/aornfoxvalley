from django.contrib import admin

from aornfoxvalley.events.models import Event, Place
from aornfoxvalley.events.forms import PlaceForm
from aornfoxvalley.events.admin_select import NiceUserModelAdmin


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'address_1', 'address_2', 'city', 'state',)
    list_filter = ('title', 'city', 'state',)
    prepopulated_fields = {'slug': ('title',)}
    form = PlaceForm
    fieldsets = (
        (None, {
            'fields': ('title', 'slug',)
        }),
        ('Address', {
            'fields': ('address_1', 'address_2', 'city', ('state', 'zip_code'), ('province', 'postal_code'), 'country',)
        }),
        ('Media', {
            'fields': ('image', 'url',)
        }),
        ('Delete files', {
            'classes': ('collapse',),
            'fields': ('remove_image',)
        }),
    )

class EventAdmin(NiceUserModelAdmin):
    list_display = ('title', 'date_time', 'place',)
    list_filter = ('author', 'date_time',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author',)
        }),
        ('Event time', {
            'fields': (('date_time', 'date_time_end'),)
        }),
        ('Event place', {
            'fields': ('place',)
        }),
        ('Event details', {
            'fields': ('body',)
        }),
        ('Meeting details', {
            'fields': ('topic', 'speaker',)
        }),
        ('Media', {
            'fields': ('image', 'url',)
        }),
        ('Visibility', {
            'classes': ('collapse',),
            'fields': ('public', 'published',)
        }),
        ('Delete files', {
            'classes': ('collapse',),
            'fields': ('remove_image',)
        }),
    )

    class Media:
        css = {
            'all': ('adminplus/css/style.css',)
        }
        js = ('adminplus/js/jquery.min.js', 'adminplus/js/jquery.markitup.js', 'adminplus/js/jquery.adminplus.js',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Event, EventAdmin)

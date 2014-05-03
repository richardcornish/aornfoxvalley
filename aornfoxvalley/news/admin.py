from django.contrib import admin

from aornfoxvalley.news.models import Announcement
from aornfoxvalley.news.admin_select import NiceUserModelAdmin


class AnnouncementAdmin(NiceUserModelAdmin):
    list_display = ('title', 'author', 'published', 'public',)
    list_filter = ('author', 'published', 'public',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author',)
        }),
        ('Details', {
            'fields': ('body', 'image', 'url',)
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


admin.site.register(Announcement, AnnouncementAdmin)

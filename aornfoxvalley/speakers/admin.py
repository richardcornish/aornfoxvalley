from django.contrib import admin

from aornfoxvalley.speakers.models import Speaker


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title',)
    prepopulated_fields = {'slug': ('first_name', 'last_name',)}
    search_fields = ('first_name', 'last_name', 'bio',)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'slug', 'title', 'bio', 'image', 'url',)
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


admin.site.register(Speaker, SpeakerAdmin)

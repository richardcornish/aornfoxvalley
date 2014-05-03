from django.contrib import admin

from aornfoxvalley.records.models import Category, Record
from aornfoxvalley.records.admin_select import NiceUserModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug',)
        }),
    )


class RecordAdmin(NiceUserModelAdmin):
    list_display = ('title', 'category', 'published', 'public',)
    list_filter = ('category', 'published', 'public',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'slug', 'author',)
        }),
        ('Details', {
            'fields': ('document', 'body',)
        }),
        ('Visibility', {
            'classes': ('collapse',),
            'fields': ('public', 'published',)
        }),
        ('Delete files', {
            'classes': ('collapse',),
            'fields': ('remove_document',)
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Record, RecordAdmin)

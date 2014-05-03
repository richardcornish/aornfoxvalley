from django.contrib import admin

from aornfoxvalley.links.models import Category, Link


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug',)
        }),
    )


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published', 'public',)
    list_filter = ('category', 'published', 'public',)
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'url',)
        }),
        ('Visibility', {
            'classes': ('collapse',),
            'fields': ('public', 'published',)
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)

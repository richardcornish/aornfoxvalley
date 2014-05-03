from django.contrib import admin

from aornfoxvalley.members.models import Office, Committee, Member


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug',)
        }),
    )

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug',)
        }),
    )


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    list_filter = ('offices', 'committees',)
    prepopulated_fields = {'slug': ('first_name', 'last_name',)}
    search_fields = ('first_name', 'last_name',)
    filter_horizontal = ('offices', 'committees',)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'slug',)
        }),
        ('Details', {
            'fields': ('email', 'photo', 'offices', 'committees',)
        }),
        ('Visibility', {
            'classes': ('collapse',),
            'fields': ('public',)
        }),
    )


admin.site.register(Office, OfficeAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Member, MemberAdmin)

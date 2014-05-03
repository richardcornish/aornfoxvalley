from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.sites.models import Site


class MyFlatPageAdmin(FlatPageAdmin):
    class Media:
        css = {
            'all': ('adminplus/css/style.css',)
        }
        js = ('adminplus/js/jquery.min.js', 'adminplus/js/jquery.markitup.js', 'adminplus/js/jquery.adminplus.js',)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # AORN
    url(r'^news/', include('aornfoxvalley.news.urls')),
    url(r'^events/', include('aornfoxvalley.events.urls')),
    url(r'^speakers/', include('aornfoxvalley.speakers.urls')),
    url(r'^records/', include('aornfoxvalley.records.urls')),
    url(r'^feeds/', include('aornfoxvalley.feeds.urls')),
    url(r'^', include('aornfoxvalley.sitemaps.urls')),
    url(r'^$', 'aornfoxvalley.views.home', name='home'),

    # Admin password reset
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    # Admin
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/admin/'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Robots
    url(r'^robots\.txt$', include('robots.urls')),

)

# Custom 500 error handler to render {{ site }}
handler500 = 'aornfoxvalley.views.server_error'

# Static/media for local development
if getattr(settings, 'DEBUG', False):
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

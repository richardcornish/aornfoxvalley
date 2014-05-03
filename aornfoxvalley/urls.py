from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Robots
    url(r'^robots\.txt$', include('robots.urls')),

    # AORN
    url(r'^news/', include('aornfoxvalley.news.urls')),
    url(r'^events/', include('aornfoxvalley.events.urls')),
    url(r'^speakers/', include('aornfoxvalley.speakers.urls')),
    url(r'^records/', include('aornfoxvalley.records.urls')),
    url(r'^feeds/', include('aornfoxvalley.feeds.urls')),
    url(r'^', include('aornfoxvalley.sitemaps.urls')),
    url(r'^$', 'aornfoxvalley.views.home', name='home'),

)

handler500 = 'aornfoxvalley.views.server_error'

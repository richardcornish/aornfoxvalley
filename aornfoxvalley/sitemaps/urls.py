from django.conf.urls import patterns, url, include
from django.contrib.sitemaps import GenericSitemap, FlatPageSitemap

from aornfoxvalley.news.models import Announcement
from aornfoxvalley.events.models import Event
from aornfoxvalley.speakers.models import Speaker


announcement_dict = {
    'queryset': Announcement.objects.is_published(),
    'date_field': 'published',
}

event_dict = {
    'queryset': Event.objects.is_published(),
    'date_field': 'date_time',
}

sitemaps = {
    'announcement': GenericSitemap(announcement_dict, priority=0.5),
    'event': GenericSitemap(event_dict, priority=0.5),
    'flatpages': FlatPageSitemap,
}


urlpatterns = patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)

from django.conf.urls import patterns, url, include

from aornfoxvalley.feeds.news import AnnouncementsFeed
from aornfoxvalley.feeds.events import EventsFeed


urlpatterns = patterns('',

    # Announcements feed
    url(r'^news/$',
        AnnouncementsFeed(),
        name='news_announcement_feed'
    ),

    # Events feed
    url(r'^events/$',
        EventsFeed(),
        name='events_event_feed'
    ),

)

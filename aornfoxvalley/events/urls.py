from django.conf.urls import patterns, url, include


urlpatterns = patterns('aornfoxvalley.events.views',

    # Past event list
    url(r'^past/$',
        view='past_event_list_view',
        name='events_past_event_list'
    ),

    # Event detail iCal
    url(r'^(?P<slug>[-\w]+)/ical/$',
        view='event_ical_view',
        name='events_event_ical'
    ),

    # Event detail Outlook
    url(r'^(?P<slug>[-\w]+)/vcs/$',
        view='event_outlook_view',
        name='events_event_outlook'
    ),

    # Event detail
    url(r'^(?P<slug>[-\w]+)/$',
        view='event_detail_view',
        name='events_event_detail'
    ),

    # Event list
    url(r'^$',
        view='event_list_view',
        name='events_event_list'
    ),

)

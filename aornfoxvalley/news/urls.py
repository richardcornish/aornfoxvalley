from django.conf.urls import patterns, url, include


urlpatterns = patterns('aornfoxvalley.news.views',

    # Announcement detail
    url(r'^(?P<slug>[-\w]+)/$',
        view='announcement_detail_view',
        name='news_announcement_detail'
    ),

    # Announcement list
    url(r'^$',
        view='announcement_list_view',
        name='news_announcement_list'
    ),

)

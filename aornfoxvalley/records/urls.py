from django.conf.urls import patterns, url, include


urlpatterns = patterns('aornfoxvalley.records.views',

    # Record list
    url(r'^$',
        view='record_list_view',
        name='records_record_list'
    ),

)

from django.conf.urls import patterns, url, include


urlpatterns = patterns('aornfoxvalley.speakers.views',

    # Speaker list
    url(r'^$',
        view='speaker_list_view',
        name='speakers_speaker_list'
    ),

)

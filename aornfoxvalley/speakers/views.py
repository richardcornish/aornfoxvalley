from django.views.generic import ListView

from aornfoxvalley.speakers.models import Speaker


class SpeakerListView(ListView):
    queryset = Speaker.objects.is_published()

speaker_list_view = SpeakerListView.as_view()

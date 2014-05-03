from django.views.generic import ListView
from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext

from aornfoxvalley.news.models import Announcement
from aornfoxvalley.events.models import Event

import os


class HomeView(ListView):
    queryset = Announcement.objects.is_published()[:5]
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.is_future()[:5]
        return context
home = HomeView.as_view()


def server_error(request, template_name='500.html'):
    return render_to_response(
        template_name,
        context_instance = RequestContext(request)
    )

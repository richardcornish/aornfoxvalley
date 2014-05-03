from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib.sites.models import Site

from aornfoxvalley.events.models import Event

import re


class EventListView(ListView):
    queryset = Event.objects.is_future()

event_list_view = EventListView.as_view()


class PastEventListView(ListView):
    queryset = Event.objects.is_past()
    template_name = 'events/past_event_list.html'

past_event_list_view = PastEventListView.as_view()


class EventDetailView(DetailView):
    queryset = Event.objects.is_published()

    def get_context_data(self, **kwargs):
        if re.search('(iPhone|iPad|iPod)', self.request.META['HTTP_USER_AGENT']):
            maps_service = u'%s' % ('apple')
        else:
            maps_service = u'%s' % ('google')
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['maps_service'] = maps_service
        return context

event_detail_view = EventDetailView.as_view()


class EventIcalView(DetailView):
    queryset = Event.objects.is_published()
    template_name = 'events/event_ical.html'

    def render_to_response(self, context, **kwargs):
        return super(EventIcalView, self).render_to_response(context, content_type='text/calendar', **kwargs)

event_ical_view = EventIcalView.as_view()


class EventOutlookView(DetailView):
    queryset = Event.objects.is_published()
    template_name = 'events/event_outlook.html'

    def render_to_response(self, context, **kwargs):
        return super(EventOutlookView, self).render_to_response(context, content_type='text/x-vcalendar', **kwargs)

event_outlook_view = EventOutlookView.as_view()

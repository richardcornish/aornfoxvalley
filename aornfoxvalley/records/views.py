from django.views.generic import ListView
from django.db.models import Q

from aornfoxvalley.records.models import Category, Record


class RecordListView(ListView):
    queryset = Record.objects.is_public().exclude(Q(category__title='By-laws') | Q(category__title='Policy manuals')).order_by('category__title', 'title')

    def get_context_data(self, **kwargs):
        context = super(RecordListView, self).get_context_data(**kwargs)
        context['bylaw'] = Record.objects.is_public().filter(category__title='By-laws')[0]
        context['policy'] = Record.objects.is_public().filter(category__title='Policy manuals')[0]
        return context

record_list_view = RecordListView.as_view()

from django.views.generic import ListView, DetailView

from aornfoxvalley.news.models import Announcement


class AnnouncementListView(ListView):
    queryset = Announcement.objects.is_published()

announcement_list_view = AnnouncementListView.as_view()


class AnnouncementDetailView(DetailView):
    queryset = Announcement.objects.is_published()

announcement_detail_view = AnnouncementDetailView.as_view()

from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from aornfoxvalley.events.models import Event


class EventsFeed(Feed):

    title_template = "feeds/obj_title.html"
    description_template = "feeds/obj_description.html"

    def title(self):
        return u"%s's events" % Site.objects.get_current().name

    def description(self):
        return u"RSS feed for %s's events" % Site.objects.get_current().name

    def link(self):
        return reverse('events_event_list')

    def items(self):
        return Event.objects.is_published()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_pubdate(self, item):
        return item.published

from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from aornfoxvalley.news.models import Announcement


class AnnouncementsFeed(Feed):

    title_template = "feeds/obj_title.html"
    description_template = "feeds/obj_description.html"

    def title(self):
        return u"%s's news" % Site.objects.get_current().name

    def description(self):
        return u"RSS feed for %s's news" % Site.objects.get_current().name

    def link(self):
        return reverse('news_announcement_list')

    def items(self):
        return Announcement.objects.is_published()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_pubdate(self, item):
        return item.published

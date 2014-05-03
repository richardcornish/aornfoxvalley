from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django_localflavor_us.us_states import US_STATES

from aornfoxvalley.events import managers
from aornfoxvalley.speakers.models import Speaker

import re
import datetime


class Place(models.Model):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)
    address_1 = models.CharField(_("address 1"), max_length=255, help_text=_("Main street address, e.g. \"123 N Main St\""))
    address_2 = models.CharField(_("address 2"), blank=True, max_length=255, help_text=_("Secondary address, e.g. \"Suite 100\""))
    city = models.CharField(_("city"), max_length=255)
    state = models.CharField(_("state"), choices=US_STATES, max_length=255, default="IL", blank=True)
    zip_code = models.CharField("ZIP code", max_length=10, blank=True, help_text=_("If in the U.S., enter a ZIP code."))
    province = models.CharField(_("province"), max_length=255, blank=True, help_text=_("If <em>not</em> in the U.S., enter a province."))
    postal_code = models.CharField(_("postal code"), blank=True, max_length=255)
    country = models.CharField(_("country"), max_length=255, blank=True, default="United States")
    image = models.ImageField(_("image"), upload_to="events/images/", blank=True, null=True)
    remove_image = models.BooleanField(_("remove image"), help_text=_("Check and save to delete uploaded file."))
    url = models.URLField(_("URL"), blank=True, help_text=_("Place's official website, if there is one."))

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ["state", "city", "title"]
        verbose_name = _("place")
        verbose_name_plural = _("places")

    def __unicode__(self):
        if self.address_2 and self.address_1:
            address = u"%s, %s" % (self.address_2, self.address_1)
        else:
            address = u"%s" % (self.address_1)

        if self.province:
            return u"%s, %s, %s, %s %s, %s" % (self.title, address, self.city, self.province, self.postal_code, self.country)
        else:
            return u"%s, %s, %s, %s %s" % (self.title, address, self.city, self.state, self.zip_code)

    def address_full(self):
        if self.address_2 and self.address_1:
            return u"%s, %s" % (self.address_2, self.address_1)
        else:
            return u"%s" % (self.address_1)

    def address_basic(self):
        return u"%s" % (self.address_1)

    def website(self):
        domain = re.sub(r"(http|https)://(?:www\.)", "", self.url)
        pretty = re.sub(r"\/$", "", domain)
        return u"%s" % (pretty)


class Event(models.Model):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)
    author = models.ForeignKey(User)
    topic = models.CharField(_("topic"), blank=True, max_length=255, help_text=_("If event is a meeting, enter a topic. Could be same as event title."))
    speaker = models.ForeignKey(Speaker, blank=True, null=True)
    date_time = models.DateTimeField(_("start date and time"), default=timezone.now)
    date_time_end = models.DateTimeField(_("end date and time"), blank=True, null=True, help_text=_('Optional. If left blank, end time will default to <em>one hour</em> from start time.'))
    place = models.ForeignKey(Place)
    body = models.TextField(_("body"))
    image = models.ImageField(_("image"), upload_to="events/images/", blank=True, null=True)
    remove_image = models.BooleanField(_("remove image"), help_text=_("Check and save to delete uploaded file."))
    url = models.URLField(_("URL"), blank=True, help_text=_("Event's official website, if there is one."))
    public = models.BooleanField(_("public"), default=True)
    published = models.DateTimeField(_("published"), default=timezone.now, help_text=_("Future dates will not make post public."))
    created = models.DateTimeField(_("created"), blank=True, null=True, editable=False)
    modified = models.DateTimeField(_("modified"), default=timezone.now, editable=False)

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ["-date_time"]
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __unicode__(self):
        return u"%s" % (self.title)

    def save(self, force_insert=False, force_update=False):
        self.modified = timezone.now()
        if self.remove_image and self.image != "":
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
            self.image = ""
            self.remove_image = False
        super(Event, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass

    def get_absolute_url(self):
        return reverse("events_event_detail", args=[str(self.slug)])

    def get_previous(self):
        return self.get_previous_by_date_time(public=True, published__lte=timezone.now)

    def get_next(self):
        return self.get_next_by_date_time(public=True, published__lte=timezone.now)

    def author_name(self):
        if self.author.first_name or self.author.last_name:
            return u"%s %s" % (self.author.first_name, self.author.last_name)
        else:
            return u"%s" % (self.author.username)

    def date_time_endish(self):
        if not self.date_time_end:
            return self.date_time + datetime.timedelta(hours=1)
        else:
            return self.date_time_end

    def website(self):
        domain = re.sub(r"(http|https)://(?:www\.)", "", self.url)
        pretty = re.sub(r"\/$", "", domain)
        return u"%s" % (pretty)

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

import os

from aornfoxvalley.news import managers


class Announcement(models.Model):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)
    author = models.ForeignKey(User)
    body = models.TextField(_("body"))
    image = models.ImageField(_("image"), upload_to="news/images/", blank=True, null=True)
    remove_image = models.BooleanField(_("remove image"), help_text=_("Check and save to delete uploaded file."))
    url = models.URLField(_("URL"), blank=True, help_text=_("Website with more info on announcement, if there is one."))
    public = models.BooleanField(_("public"), default=True)
    published = models.DateTimeField(_("published"), default=timezone.now, help_text=_("Future dates will not make post public."))
    created = models.DateTimeField(_("created"), blank=True, null=True, editable=False)
    modified = models.DateTimeField(_("modified"), default=timezone.now, editable=False)

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ["-published"]
        verbose_name = _("announcement")
        verbose_name_plural = _("announcements")

    def __unicode__(self):
        return u"%s" % (self.title)

    def save(self, force_insert=False, force_update=False):
        self.modified = timezone.now()
        if self.remove_image and self.image != "":
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
            self.image = ""
            self.remove_image = False
        super(Announcement, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass

    def get_absolute_url(self):
        return reverse("news_announcement_detail", args=[str(self.slug)])

    def get_previous(self):
        return self.get_previous_by_published(public=True, published__lte=timezone.now)

    def get_next(self):
        return self.get_next_by_published(public=True, published__lte=timezone.now)

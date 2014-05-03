from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from aornfoxvalley.speakers import managers

import re


class Speaker(models.Model):
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)
    title = models.CharField(_("title"), max_length=255, blank=True)
    bio = models.TextField(_("bio"), blank=True)
    image = models.ImageField(_("image"), upload_to="speakers/images/", blank=True, null=True)
    remove_image = models.BooleanField(_("remove image"), help_text=_("Check and save to delete uploaded file."))
    url = models.URLField(_("URL"), blank=True, help_text=_("Website with more info on speaker."))
    public = models.BooleanField(_("public"), default=True)
    published = models.DateTimeField(_("published"), default=timezone.now, help_text=_("Future dates will not make post public."))
    created = models.DateTimeField(_("created"), blank=True, null=True, editable=False)
    modified = models.DateTimeField(_("modified"), default=timezone.now, editable=False)

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = _("speaker")
        verbose_name_plural = _("speakers")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def save(self, force_insert=False, force_update=False):
        self.modified = timezone.now()
        if self.remove_image and self.image != "":
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
            self.image = ""
            self.remove_image = False
        super(Speaker, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass

    def name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def website(self):
        domain = re.sub(r"(http|https)://(?:www\.)", "", self.url)
        pretty = re.sub(r"\/$", "", domain)
        return u"%s" % (pretty)

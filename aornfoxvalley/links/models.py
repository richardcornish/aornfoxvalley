from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from aornfoxvalley.links import managers


class Category(models.Model):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)

    class Meta:
        ordering = ["title"]
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __unicode__(self):
        return u"%s" % (self.title)


class Link(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(_("title"), max_length=255)
    url = models.URLField(_("URL"))
    public = models.BooleanField(_("public"), default=True)
    published = models.DateTimeField(_("published"), default=timezone.now, help_text=_("Future dates will not make post public."))
    created = models.DateTimeField(_("created"), blank=True, null=True, editable=False)
    modified = models.DateTimeField(_("modified"), default=timezone.now, editable=False)

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ["title"]
        verbose_name = _("link")
        verbose_name_plural = _("links")

    def __unicode__(self):
        return u"%s" % (self.title)

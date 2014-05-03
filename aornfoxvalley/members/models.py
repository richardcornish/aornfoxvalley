from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from aornfoxvalley.members import managers


class Office(models.Model):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)

    class Meta:
        ordering = ["id"]
        verbose_name = _("office")
        verbose_name_plural = _("offices")

    def __unicode__(self):
        return u"%s" % (self.title)


class Committee(models.Model):
    title = models.CharField(_("title"), max_length=255, help_text=_("Nominating committee, etc."))
    slug = models.SlugField(_("slug"), unique=True)

    class Meta:
        ordering = ["title"]
        verbose_name = _("committee")
        verbose_name_plural = _("committees")

    def __unicode__(self):
        return u"%s" % (self.title)


class Member(models.Model):
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)
    email = models.EmailField(_("email"), max_length=75, blank=True)
    photo = models.ImageField(_("photo"), upload_to="members/images/", blank=True, null=True)
    offices = models.ManyToManyField(Office, blank=True, null=True)
    committees = models.ManyToManyField(Committee, blank=True, null=True)
    public = models.BooleanField(_("public"), default=True)
    created = models.DateTimeField(_("created"), blank=True, null=True, editable=False)
    modified = models.DateTimeField(_("modified"), default=timezone.now, editable=False)

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = _("member")
        verbose_name_plural = _("members")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def name(self):
        return u"%s %s" % (self.first_name, self.last_name)

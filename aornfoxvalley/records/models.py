from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from aornfoxvalley.records import managers


class Category(models.Model):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)

    class Meta:
        ordering = ["title"]
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __unicode__(self):
        return u"%s" % (self.title)


class Record(models.Model):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), unique=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    document = models.FileField(_("document"), upload_to="records/documents/", blank=True, null=True)
    remove_document = models.BooleanField(_("remove document"), help_text=_("Check and save to delete uploaded file."))
    body = models.TextField(_("body"), blank=True)
    public = models.BooleanField(_("public"), default=True)
    published = models.DateTimeField(_("published"), default=timezone.now, help_text=_("Future dates will not make post public."))
    created = models.DateTimeField(_("created"), blank=True, null=True, editable=False)
    modified = models.DateTimeField(_("modified"), default=timezone.now, editable=False)

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ["category", "title", "-published"]
        verbose_name = _("record")
        verbose_name_plural = _("records")

    def __unicode__(self):
        return u"%s" % (self.title)

    def save(self, force_insert=False, force_update=False):
        self.modified = timezone.now()
        if self.remove_document and self.document != "":
            if os.path.exists(self.document.path):
                os.remove(self.document.path)
            self.document = ""
            self.remove_document = False
        super(Record, self).save(force_insert, force_update)

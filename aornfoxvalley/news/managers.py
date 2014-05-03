from django.db import models
from django.utils import timezone


class VisibilityManager(models.Manager):
    def is_public(self):
        return self.get_query_set().filter(public=True).order_by('-published')

    def is_published(self):
        return self.get_query_set().filter(public=True, published__lte=timezone.now).order_by('-published')

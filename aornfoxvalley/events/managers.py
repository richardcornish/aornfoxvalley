from django.db import models
from django.utils import timezone


class VisibilityManager(models.Manager):
    def is_public(self):
        return self.get_query_set().filter(public=True).order_by('-published')

    def is_published(self):
        return self.get_query_set().filter(public=True, published__lte=timezone.now).order_by('-published')

    def is_future(self):
        return self.get_query_set().filter(public=True, published__lte=timezone.now, date_time__gt=timezone.now).order_by('date_time')

    def is_past(self):
        return self.get_query_set().filter(public=True, published__lte=timezone.now, date_time__lt=timezone.now).order_by('-date_time')

from django.db import models
from django.utils import timezone


class VisibilityManager(models.Manager):
    def is_public(self):
        return self.get_query_set().filter(public=True)

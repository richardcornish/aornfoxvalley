from django import template

from aornfoxvalley.members.models import Committee


register = template.Library()


def get_committees():
    return Committee.objects.filter(member__isnull=False).distinct()


register.assignment_tag(get_committees)

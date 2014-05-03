from django import template

from aornfoxvalley.members.models import Office


register = template.Library()


def get_offices():
    return Office.objects.filter(member__isnull=False).distinct()


register.assignment_tag(get_offices)

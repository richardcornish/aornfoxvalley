from django import template

from aornfoxvalley.members.models import Member


register = template.Library()


def get_members():
    return Member.objects.is_public()


register.assignment_tag(get_members)

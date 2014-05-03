from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
def add_break(text):
    """
    Add an extra break (\n) between paragraphs.
    Useful for additional formatting after markdown/striptags
    """
    return mark_safe(text.replace('\n', '\n\n'))

add_break = stringfilter(add_break)
register.filter(add_break)

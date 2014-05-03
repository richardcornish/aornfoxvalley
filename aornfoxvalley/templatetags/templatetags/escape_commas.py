from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
def escape_commas(text):
    """
    Escapes all commas with a backslash.
    """
    return mark_safe(text.replace(',', '\,'))

escape_commas = stringfilter(escape_commas)
register.filter(escape_commas)

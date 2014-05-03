from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def plusify(value):
    """
    Replace a string's space (" "/"%20") or encoded plus ("%2B")
    with a plus sign ("+") for use in Google Maps.

    Use {{ obj.address|urlencode|plusify }}

    """
    plusified = value.replace(" ", "+").replace("%20", "+").replace("%2B", "+")
    return plusified

register.filter("plusify", plusify)

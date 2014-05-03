from django import template

from aornfoxvalley.links.models import Link


register = template.Library()


class LinkListNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = Link.objects.is_public()
        return ''


def get_links(parser, token):
    bits = token.split_contents()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("%r tag requires two arguments" % token.contents.split()[0])
    if bits[1] != 'as':
        raise template.TemplateSyntaxError("First argument to %r tag must be 'as'" % token.contents.split()[0])
    return LinkListNode(bits[2])


register.tag(get_links)

from django.template import RequestContext
from django.contrib.sites.models import Site

from django.conf import settings


def get_site(request):
    return {
        'site': Site.objects.get_current()
    }


def get_email(request):
    return {
        'email': settings.CONTACT_EMAIL
    }

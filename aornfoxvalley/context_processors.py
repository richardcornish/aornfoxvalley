from django.contrib.sites.models import get_current_site

from django.conf import settings


def site(request):
    """
    Gets current website and adds it to the template context.
    """
    return {'site': get_current_site(request)}


def email(request):
    """
    Gets contact email address and adds it to the template context.
    """
    email = getattr(settings, 'AORN_CONTACT_EMAIL', '')

    return {'EMAIL': email}

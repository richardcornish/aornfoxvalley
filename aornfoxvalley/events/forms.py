from django import forms
from django_localflavor_us.forms import USZipCodeField

from aornfoxvalley.events.models import Place


class PlaceForm(forms.ModelForm):
    zip_code = USZipCodeField(label='ZIP code', required=False)

    class Meta:
        model = Place

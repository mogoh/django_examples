from django import forms
from django.forms import ModelForm

from dal.autocomplete import Select2
from dal.autocomplete import ModelSelect2

from .models import Autocomplete_Light


class Autocomplete_Light_Form(ModelForm):
    class Meta:
        model = Autocomplete_Light
        fields = ('text',)
        widgets = {
            'text': ModelSelect2(url='autocomplete-example')
        }

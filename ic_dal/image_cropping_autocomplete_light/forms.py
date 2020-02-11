from dal import autocomplete
from django.forms import ModelForm

from .models import Image_Cropping_Autocomplete_Light


class Image_Cropping_Autocomplete_Light_Form(ModelForm):
    class Meta:
        model = Image_Cropping_Autocomplete_Light
        fields = '__all__'
        widgets = {
            'text': autocomplete.Select2(url='autocomplete-example')
        }

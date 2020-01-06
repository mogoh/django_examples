from django.contrib.admin import register
from django.contrib.admin import ModelAdmin

from .models import Autocomplete_Light
from .forms import Autocomplete_Light_Form


@register(Autocomplete_Light)
class Autocomplete_Light_Admin(ModelAdmin):
    form = Autocomplete_Light_Form

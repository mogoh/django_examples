from django.contrib.admin import ModelAdmin
from django.contrib.admin import register

from image_cropping import ImageCroppingMixin

from .models import Image_Cropping_Autocomplete_Light
from .forms import Image_Cropping_Autocomplete_Light_Form


@register(Image_Cropping_Autocomplete_Light)
class Image_Cropping_Autocomplete_Light_Admin(ImageCroppingMixin, ModelAdmin):
    form = Image_Cropping_Autocomplete_Light_Form

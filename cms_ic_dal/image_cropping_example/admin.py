from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Image_Cropping


@admin.register(Image_Cropping)
class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
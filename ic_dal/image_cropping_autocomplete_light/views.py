from django.shortcuts import render

from dal import autocomplete

from .models import Image_Cropping_Autocomplete_Light


class Autocomplete_Light_Autocomplete(autocomplete.Select2QuerySetView):
    create_field = 'text'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Image_Cropping_Autocomplete_Light.objects.none()

        qs = Image_Cropping_Autocomplete_Light.objects.all()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs

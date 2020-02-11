from django.shortcuts import render

from dal.autocomplete import Select2QuerySetView

from .models import Autocomplete_Light


class Autocomplete_Light_Autocomplete(Select2QuerySetView):
    create_field = 'text'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Autocomplete_Light.objects.none()

        qs = Autocomplete_Light.objects.all()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs

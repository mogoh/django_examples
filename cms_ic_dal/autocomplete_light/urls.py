from django.conf.urls import include
from django.conf.urls import url

from .views import Autocomplete_Light_Autocomplete

urlpatterns = [
    url(
        r'^$',
        Autocomplete_Light_Autocomplete.as_view(),
        name='autocomplete-example',
    ),
]

from django.db.models import Model
from django.db.models import CharField


class Autocomplete_Light(Model):
    text = CharField(max_length=255)

    def __str__(self):
        return self.text

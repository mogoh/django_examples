from django.db.models import Model
from django.db.models import CharField
from image_cropping import ImageCropField
from image_cropping import ImageRatioField

class Image_Cropping_Autocomplete_Light(Model):
    text = CharField(max_length=255)
    image = ImageCropField(
        "image",
        blank=True,
        null=True,
        upload_to='uploaded_images',
    )
    image_cropped = ImageRatioField(
        'image',
        '430x360',
    )

    def __str__(self):
        return self.text

from django.db.models import Model
from image_cropping import ImageCropField
from image_cropping import ImageRatioField


class Image_Cropping(Model):
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
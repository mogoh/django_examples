# Generated by Django 2.2.9 on 2020-01-06 16:44

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    replaces = [('image_cropping_example', '0001_initial'), ('image_cropping_example', '0002_auto_20191220_1510'), ('image_cropping_example', '0003_auto_20200106_1350'), ('image_cropping_example', '0004_auto_20200106_1352')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Cropping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', image_cropping.fields.ImageCropField(blank=True, null=True, upload_to='uploaded_images', verbose_name='image')),
                ('image_cropped', image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image cropped')),
            ],
        ),
    ]
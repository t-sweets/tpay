# Generated by Django 2.1.5 on 2019-02-28 18:35

import common.models
from django.db import migrations, models
import media_upload.models
import ulid.api


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', common.models.ULIDField(default=ulid.api.new, editable=False, max_length=26, primary_key=True, serialize=False, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('image', models.ImageField(height_field='height', upload_to=media_upload.models.Image.get_image_path, verbose_name='image', width_field='width')),
                ('height', models.IntegerField(editable=False)),
                ('width', models.IntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
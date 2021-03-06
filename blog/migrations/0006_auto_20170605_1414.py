# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 14:14
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170529_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([(b'paragraph', wagtail.core.blocks.RichTextBlock()), (b'image', wagtail.images.blocks.ImageChooserBlock()), (b'html', wagtail.core.blocks.RawHTMLBlock())]),
        ),
    ]

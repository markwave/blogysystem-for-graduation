# Generated by Django 2.2.8 on 2020-03-04 07:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogv1', '0007_auto_20200303_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogv1',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

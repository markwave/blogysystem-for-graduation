# Generated by Django 2.2.8 on 2020-02-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogv1', '0004_blogv1_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogv1',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogv1',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]

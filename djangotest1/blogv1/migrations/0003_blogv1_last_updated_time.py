# Generated by Django 2.2.8 on 2020-02-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogv1', '0002_blogv1_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogv1',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

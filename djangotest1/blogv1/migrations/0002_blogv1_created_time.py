# Generated by Django 2.2.8 on 2020-02-29 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogv1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogv1',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

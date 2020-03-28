# Generated by Django 2.2.8 on 2020-03-19 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0003_auto_20200308_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='readdetail',
            options={'verbose_name': '阅读关联', 'verbose_name_plural': '阅读关联'},
        ),
        migrations.AlterModelOptions(
            name='readnum',
            options={'verbose_name': '阅读数', 'verbose_name_plural': '阅读数'},
        ),
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='readdetail',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name='阅读数'),
        ),
        migrations.AlterField(
            model_name='readnum',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name='阅读数'),
        ),
    ]
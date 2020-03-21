# Generated by Django 2.2.8 on 2020-03-19 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogv1', '0011_auto_20200308_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogtype',
            options={'verbose_name': '博客类型', 'verbose_name_plural': '博客类型'},
        ),
        migrations.AlterModelOptions(
            name='blogv1',
            options={'ordering': ['-created_time'], 'verbose_name': '博客', 'verbose_name_plural': '博客'},
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='type_name',
            field=models.CharField(max_length=15, verbose_name='博客类型'),
        ),
        migrations.AlterField(
            model_name='blogv1',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='blogv1',
            name='blog_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogv1.BlogType', verbose_name='博客类型'),
        ),
        migrations.AlterField(
            model_name='blogv1',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创作时间'),
        ),
        migrations.AlterField(
            model_name='blogv1',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='blogv1',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最近更新时间'),
        ),
        migrations.AlterField(
            model_name='blogv1',
            name='title',
            field=models.CharField(max_length=50, verbose_name='博文标题'),
        ),
    ]

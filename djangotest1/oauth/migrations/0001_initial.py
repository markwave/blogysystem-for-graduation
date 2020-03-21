# Generated by Django 2.2.8 on 2020-03-20 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuth_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=12)),
                ('img', models.FileField(upload_to='static/img/connect')),
                ('client_id', models.CharField(default='', max_length=24)),
                ('client_secret', models.CharField(default='', max_length=48)),
                ('redirect_uri', models.URLField(default='')),
                ('scope', models.CharField(default='', max_length=24)),
                ('url_authorize', models.URLField(blank=True, default='')),
                ('url_access_token', models.URLField(blank=True, default='')),
                ('url_open_id', models.URLField(blank=True, default='')),
                ('url_user_info', models.URLField(blank=True, default='')),
                ('url_email', models.URLField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='OAuth_ex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=64)),
                ('oauth_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='oauth.OAuth_type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='第三方用户')),
            ],
        ),
    ]

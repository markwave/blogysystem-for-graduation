from django.contrib import admin

# Register your models here.
#coding:utf-8

from .models import Notice
 
@admin.register(Notice)
class BlogAdmin(admin.ModelAdmin):
    """blog admin"""
    list_display=('id','content','create_time')
 
    #filter date
    date_hierarchy='create_time'
    ordering=('-create_time',)
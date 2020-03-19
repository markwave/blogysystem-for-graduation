from django.db import models

# Create your models here.
#coding:utf-8

 
class Notice(models.Model):
    content = models.TextField(verbose_name='消息')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='消息时间')
    
    def __unicode__(self):
        return u'%s' % (self.content)
 
    class Meta:
        ordering=['-create_time']

        verbose_name='消息提醒'
        verbose_name_plural=verbose_name
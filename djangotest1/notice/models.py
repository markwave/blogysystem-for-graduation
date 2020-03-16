from django.db import models

# Create your models here.
#coding:utf-8

 
class Notice(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s' % (self.content)
 
    class Meta:
        ordering=['-create_time']
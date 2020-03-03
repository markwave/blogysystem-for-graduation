from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogType(models.Model):
	type_name=models.CharField(max_length=15)

	def __str__(self):
		return self.type_name

	



class blogv1(models.Model):
	title=models.CharField(max_length=50)
	content=models.TextField()
	created_time=models.DateTimeField(auto_now_add=True)
	last_updated_time=models.DateTimeField(auto_now=True)
	author=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1) 
	is_deleted=models.BooleanField(default=False)
	read_num= models.IntegerField(default=0)
	blog_type=models.ForeignKey(BlogType,on_delete=models.DO_NOTHING,default=1)
	def __str__(self):
		return "Article:%s" % self.title

from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from read_statistics.models import ReadNumExpandMethod,ReadDetail
# Create your models here.
class BlogType(models.Model):
	type_name=models.CharField(max_length=15)

	def __str__(self):
		return self.type_name

	



class blogv1(models.Model,ReadNumExpandMethod):
	title=models.CharField(max_length=50)
	content=RichTextUploadingField()
	created_time=models.DateTimeField(auto_now_add=True)
	last_updated_time=models.DateTimeField(auto_now=True)
	author=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1) 
	is_deleted=models.BooleanField(default=False)
	read_details = GenericRelation(ReadDetail)
	blog_type=models.ForeignKey(BlogType,on_delete=models.DO_NOTHING,default=1)
	def __str__(self):
		return "Article:%s" % self.title

	class Meta:
		ordering=['-created_time']
			
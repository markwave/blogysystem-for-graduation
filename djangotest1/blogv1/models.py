from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from read_statistics.models import ReadNumExpandMethod,ReadDetail
from django.urls import reverse
# Create your models here.
class BlogType(models.Model):
	type_name=models.CharField(max_length=15,verbose_name='博客类型')

	def __str__(self):
		return self.type_name
	class Meta:
		
		verbose_name='博客类型'
		verbose_name_plural=verbose_name
	



class blogv1(models.Model,ReadNumExpandMethod):
	title=models.CharField(max_length=50,verbose_name='博文标题')
	content=RichTextUploadingField()
	created_time=models.DateTimeField(auto_now_add=True,verbose_name='创作时间')
	last_updated_time=models.DateTimeField(auto_now=True,verbose_name='最近更新时间')
	author=models.ForeignKey(User,on_delete=models.CASCADE,default=1,verbose_name='作者') 
	is_deleted=models.BooleanField(default=False,verbose_name='是否删除')
	read_details = GenericRelation(ReadDetail)
	blog_type=models.ForeignKey(BlogType,on_delete=models.CASCADE,default=1,verbose_name='博客类型')
	def get_url(self):
		return reverse('article_detail', kwargs={'b_id': self.pk})

	def get_email(self):
		return self.author.email
	def get_user(self):
		return self.author
	def __str__(self):
		return "Article:%s" % self.title

	class Meta:
		ordering=['-created_time']
		verbose_name='博客'
		verbose_name_plural=verbose_name
			
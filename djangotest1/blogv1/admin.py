from django.contrib import admin
from .models import blogv1,BlogType
# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
	list_display=("id","type_name")	
	

@admin.register(blogv1)
class ArticleAdmin(admin.ModelAdmin):
	list_display=("id","title","blog_type","author","is_deleted", "created_time","last_updated_time")	
	

#admin.site.register(blogv1,ArticleAdmin)


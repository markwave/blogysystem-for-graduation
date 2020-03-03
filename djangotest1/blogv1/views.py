from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import blogv1,BlogType


# Create your views here.
def article_detail(request,b_id):

	article=get_object_or_404(blogv1,pk=b_id)
	context={}
	context['article_obj']=article
	return render(request,"blog/article_detail.html",context)

def article_list(request):
	articles=blogv1.objects.filter(is_deleted=False)
	context={}
	context['blogs']=articles
	context['blog_types']=BlogType.objects.all( )
	return render(request,"blog/article_list.html",context)

	
def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = blogv1.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types']=BlogType.objects.all( )
    return render(request,'blog/blogs_with_type.html', context)
	

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import blogv1,BlogType
from django.core.paginator import Paginator

# Create your views here.
def article_detail(request,b_id):

	article=get_object_or_404(blogv1,pk=b_id)
	context={}
	context['article_obj']=article
	return render(request,"blog/article_detail.html",context)

def article_list(request):
	articles=blogv1.objects.filter(is_deleted=False)
	paginator=Paginator(articles,10) #每10篇进行分页
	page_num=request.GET.get('page',1) #获取url学生页面参数 
	page_of_blogs=paginator.get_page(page_num)

	context={}
	context['blogs']=page_of_blogs.object_list
	context['blog']=page_of_blogs
	context['blog_types']=BlogType.objects.all( )
	return render(request,"blog/article_list.html",context)

	
def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = blogv1.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types']=BlogType.objects.all( )
    return render(request,'blog/blogs_with_type.html', context)
	

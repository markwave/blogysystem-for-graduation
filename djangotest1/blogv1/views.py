from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import blogv1,BlogType
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
def article_detail(request,b_id):

    article=get_object_or_404(blogv1,pk=b_id)
    context={}
    context['article_obj']=article
    context['previous_blog']=blogv1.objects.filter(created_time__gt=article.created_time).last()
    context['next_blog']=blogv1.objects.filter(created_time__lt=article.created_time).first()
    return render(request,"blog/article_detail.html",context)

def article_list(request):
    articles=blogv1.objects.filter(is_deleted=False)
    paginator=Paginator(articles,settings.EACH_PAGE_BLOGS_NUMBER) #每10篇进行分页
    page_num=request.GET.get('page',1) #获取url学生页面参数 
    page_of_blogs=paginator.get_page(page_num)
    currentr_page_num=page_of_blogs.number#获取当前页码
    page_range=list(range(max(currentr_page_num-2,1),currentr_page_num))+\
                list(range(currentr_page_num,min(currentr_page_num+2,paginator.num_pages)+1))
    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1]>=2:
        page_range.append('...')
    if page_range[0]!=1:
        page_range.insert(0,1)
    if page_range[-1]!=paginator.num_pages:
        page_range.append(paginator.num_pages)
    context={}
    context['blogs']=page_of_blogs.object_list
    context['blog']=page_of_blogs
    context['page_range']=page_range
    context['blog_dates']=blogv1.objects.dates('created_time','month',order="DESC")
    context['blog_types']=BlogType.objects.all( )
    return render(request,"blog/article_list.html",context)

	
def blogs_with_type(request, blog_type_pk):
    
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    articles=blogv1.objects.filter(blog_type=blog_type)
    paginator=Paginator(articles,settings.EACH_PAGE_BLOGS_NUMBER) #每10篇进行分页
    page_num=request.GET.get('page',1)
    page_of_blogs=paginator.get_page(page_num)
    currentr_page_num=page_of_blogs.number#获取当前页码
    page_range=list(range(max(currentr_page_num-2,1),currentr_page_num))+\
               list(range(currentr_page_num,min(currentr_page_num+2,paginator.num_pages)+1))
    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1]>=2:
        page_range.append('...')
    if page_range[0]!=1:
        page_range.insert(0,1)
    if page_range[-1]!=paginator.num_pages:
        page_range.append(paginator.num_pages)
    context={}
    context['blogs']=page_of_blogs.object_list
    context['blog']=page_of_blogs
    context['blog_type'] = blog_type
    context['blog_dates']=blogv1.objects.dates('created_time','month',order="DESC")
    context['page_range']=page_range
    context['blog_types']=BlogType.objects.all( )
    return render(request,'blog/blogs_with_type.html', context)
	


def blogs_with_date(request,year,month):
   
    articles=blogv1.objects.filter(created_time__year=year,created_time__month=month)
    paginator=Paginator(articles,settings.EACH_PAGE_BLOGS_NUMBER) #每10篇进行分页
    page_num=request.GET.get('page',1)
    page_of_blogs=paginator.get_page(page_num)
    currentr_page_num=page_of_blogs.number#获取当前页码
    page_range=list(range(max(currentr_page_num-2,1),currentr_page_num))+\
               list(range(currentr_page_num,min(currentr_page_num+2,paginator.num_pages)+1))
    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1]>=2:
        page_range.append('...')
    if page_range[0]!=1:
        page_range.insert(0,1)
    if page_range[-1]!=paginator.num_pages:
        page_range.append(paginator.num_pages)
    context={}
    context['blogs']=page_of_blogs.object_list
    context['blog']=page_of_blogs
    context['blogs_with_date']='%s年%s月' % (year,month)
    context['blog_dates']=blogv1.objects.dates('created_time','month',order="DESC")
    context['page_range']=page_range
    context['blog_types']=BlogType.objects.all( )
    return render(request,'blog/blogs_with_date.html', context)

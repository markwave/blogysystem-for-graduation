
from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,Http404
from .models import blogv1,BlogType
from django.core.paginator import Paginator
from django.db.models import Count
from django.conf import settings
from read_statistics.utils import read_statistics_once_read
import random
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def get_blog_list_common_data(request,articles):
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

#日期归档数量
    blog_dates=blogv1.objects.dates('created_time','month',order="DESC")
    blog_dates_dict={}
    for blog_date in blog_dates:
        blog_count=blogv1.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date]=blog_count

#随机推荐模块
    rand_count = 10
    randomblogs = random.sample(list(blogv1.objects.all()), rand_count)

    context={}
    context['blogs']=page_of_blogs.object_list
    context['blog']=page_of_blogs
    context['page_range']=page_range
    context['blog_dates']=blog_dates_dict
    context['rand_blogs']=randomblogs
    context['blog_types']=BlogType.objects.annotate(blog_count=Count('blogv1'))
    return context    
def article_detail(request,b_id):

    article=get_object_or_404(blogv1,pk=b_id)
    read_cookie_key = read_statistics_once_read(request, article)

    context={}
    context['article_obj']=article
    context['previous_blog']=blogv1.objects.filter(created_time__gt=article.created_time).last()
    context['next_blog']=blogv1.objects.filter(created_time__lt=article.created_time).first()
  

    
    response = render(request,'blog/article_detail.html', context) # 响应
    response.set_cookie(read_cookie_key, 'true') # 阅读cookie标记
    return response

def article_list(request):
    articles=blogv1.objects.filter(is_deleted=False)
    context=get_blog_list_common_data(request,articles)

    return render(request,"blog/article_list.html",context)

	
def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    articles=blogv1.objects.filter(blog_type=blog_type)
    context=get_blog_list_common_data(request,articles)
    context['blog_type'] = blog_type
  
    return render(request,'blog/blogs_with_type.html', context)
	


def blogs_with_date(request,year,month):
   
    articles=blogv1.objects.filter(created_time__year=year,created_time__month=month)
    context=get_blog_list_common_data(request,articles)
    context['blogs_with_date']='%s年%s月' % (year,month)
    
    return render(request,'blog/blogs_with_date.html', context)

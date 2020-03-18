import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum, Q,Count
from django.core.cache import cache
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from blogv1.models import blogv1,BlogType
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse

def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = blogv1.objects \
                .filter(read_details__date__lt=today, read_details__date__gte=date) \
                .values('id', 'title') \
                .annotate(read_num_sum=Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:7]

def loading(request):
    return render(request,'index.html')
def home(request):
    blog_content_type = ContentType.objects.get_for_model(blogv1)
    dates, read_nums = get_seven_days_read_data(blog_content_type)
    # 获取7天热门博客的缓存数据
    hot_blogs_for_7_days = cache.get('hot_blogs_for_7_days')
    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_7_days_hot_blogs()
        cache.set('hot_blogs_for_7_days', hot_blogs_for_7_days, 600)


    context = {}
    context['blognum']=blogv1.objects.filter(is_deleted=False).count()
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['blog_types']=BlogType.objects.annotate(blog_count=Count('blogv1'))
    context['hot_blogs_for_7_days'] = hot_blogs_for_7_days
    return render(request,'blog/home.html', context)

def my_notifications(request):
    context = {}
    return render(request, 'my_notifications.html', context)

def search(request):
    search_words = request.GET.get('wd', '').strip()
    # 分词：按空格 & | ~
    condition = None
    for word in search_words.split(' '):
        if condition is None:
            condition = Q(title__icontains=word)
        else:
            condition = condition | Q(title__icontains=word)
    
    search_blogs = []
    if condition is not None:
        # 筛选：搜索
        search_blogs = blogv1.objects.filter(condition)

    # 分页
    paginator = Paginator(search_blogs, 10)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
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

    context = {}
    context['search_words'] = search_words
    context['page_range']=page_range
    context['search_blogs_count'] = search_blogs.count()
    context['page_of_blogs'] = page_of_blogs
    return render(request, 'search.html', context)  
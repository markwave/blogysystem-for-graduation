
from django.shortcuts import render_to_response
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import get_seven_days_read_data
from blogv1.models import blogv1

def home(request):
    blog_content_type = ContentType.objects.get_for_model(blogv1)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    return render_to_response('blog/home.html', context)
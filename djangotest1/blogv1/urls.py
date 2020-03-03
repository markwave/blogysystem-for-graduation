from django.urls import path
from . import views
from blogv1.views import article_list,article_detail

urlpatterns = [
    # http://localhost:8000/blog/1
    path('', article_list, name='article_list'),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('<int:b_id>', article_detail, name="article_detail"),


]
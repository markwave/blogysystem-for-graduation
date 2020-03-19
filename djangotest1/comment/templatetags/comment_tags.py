from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comment
from ..forms import CommentForm


register = template.Library()

@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.pk).count()

@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(initial={
            'content_type': content_type.model, 
            'object_id': obj.pk, 
            'reply_comment_id': 0})
    return form

@register.simple_tag
def get_comment_list(obj):
    content_type = ContentType.objects.get_for_model(obj)
    
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk, parent=None)
    
    return comments.order_by('-comment_time')
@register.simple_tag
def get_comment_user(obj):
    
    
    comments = Comment.objects.filter(user=obj, parent=None)
    replycomments=Comment.objects.filter(user=obj).exclude(parent=None)
    replyedcount=0
    for comment in comments:
        lll=comment.root_comment.all()
        for replyed in lll:
            replyedcount=replyedcount+1

    
    data={}
    data['replycount']=replycomments.count()
    data['commentcount']=comments.count()
    data['replyedcount']=replyedcount
    data['usercomment']=comments.order_by('-comment_time')
    data['replycomments']=replycomments.order_by('-comment_time')
    return data
    
    
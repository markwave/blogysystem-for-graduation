from django.urls import path
from . import views

urlpatterns = [
path('get_notice', views.get_notice, name='get_notice'),
]
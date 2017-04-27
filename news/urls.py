from django.conf.urls import url, include
from django.contrib import admin
from .views import (
    news_list,
    news_create,
    news_detail,
    news_update,
    news_delete
)

urlpatterns = [
    url(r'^$', news_list),
    url(r'^create/', news_create),
    url(r'^(?P<id>\d+)/$', news_detail, name='news_detail'),
    url(r'^(?P<id>\d+)/edit/', news_update, name='update'),
    url(r'^delete/', news_delete),
]
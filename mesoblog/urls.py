from django.conf.urls import patterns, url

from mesoblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.article, name='article'),
    url(r'^article/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='articleFromSlug'),
)


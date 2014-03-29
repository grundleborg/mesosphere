from django.conf.urls import patterns, url

from mesoblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.article, name='article'),
    url(r'^article/(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='articleLongForm'),
    url(r'^article/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='articleFromSlug'),
    url(r'^category/(?P<category_id>\d+)$', views.category, name='category'),
    url(r'^category/(?P<category_slug>[-\w]+)$', views.categoryFromSlug, name='categoryFromSlug'),
)


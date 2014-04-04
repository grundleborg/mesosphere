from django.conf.urls import patterns, url

from mesoblog import views

urlpatterns = patterns('',
    url(r'^(?P<page>\d+)?$', views.index, name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.article, name='article'),
    url(r'^article/(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='articleLongForm'),
    url(r'^article/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='articleFromSlug'),
    url(r'^category/(?P<category_id>\d+)(/(?P<page>\d+))?$', views.category, name='category'),
    url(r'^category/(?P<category_slug>[-\w]+)(/(?P<page>\d+))?$', views.categoryFromSlug, name='categoryFromSlug'),
    url(r'^archive/(?P<year>\d\d\d\d)/(?P<month>\d\d)(/(?P<page>\d+))?$', views.archive, name='archive'),
)


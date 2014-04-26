from django.conf.urls import patterns, url

from mesoblog import views

urlpatterns = patterns('',
    url(r'^(?P<page>\d+)?$', views.index, name='mesoblog.index'),
    url(r'^article/(?P<article_id>\d+)$', views.article, name='mesoblog.article'),
    url(r'^article/(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='mesoblog.articleLongForm'),
    url(r'^article/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='mesoblog.articleFromSlug'),
    url(r'^category/(?P<category_id>\d+)(/(?P<page>\d+))?$', views.category, name='mesoblog.category'),
    url(r'^category/(?P<category_slug>[-\w]+)(/(?P<page>\d+))?$', views.categoryFromSlug, name='mesoblog.categoryFromSlug'),
    url(r'^archive/(?P<year>\d\d\d\d)/(?P<month>\d\d)(/(?P<page>\d+))?$', views.archive, name='mesoblog.archive'),
)


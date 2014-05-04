from django.conf.urls import patterns, url

from mesoblog import views
from mesoblog.feeds import LatestArticlesRssFeed, CategoryArticlesRssFeed, TagArticlesRssFeed

urlpatterns = patterns('',
    url(r'^(?P<page>\d+)?$', views.index, name='mesoblog.index'),
    url(r'^article/(?P<article_id>\d+)$', views.article, name='mesoblog.article'),
    url(r'^article/(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='mesoblog.articleLongForm'),
    url(r'^article/(?P<article_slug>[-\w]+)$', views.articleFromSlug, name='mesoblog.articleFromSlug'),
    url(r'^category/(?P<category_id>\d+)(/(?P<page>\d+))?$', views.category, name='mesoblog.category'),
    url(r'^category/(?P<category_slug>[-\w]+)(/(?P<page>\d+))?$', views.categoryFromSlug, name='mesoblog.categoryFromSlug'),
    url(r'^archive/(?P<year>\d\d\d\d)/(?P<month>\d\d)(/(?P<page>\d+))?$', views.archive, name='mesoblog.archive'),
    url(r'^feed/rss$', LatestArticlesRssFeed(), name='mesoblog.feed.index'),
    url(r'^feed/rss/category/(?P<category_id>\d+)$', CategoryArticlesRssFeed(), name='mesoblog.feed.rss.category'),
     url(r'^feed/rss/category/(?P<category_slug>[-\w]+)$', CategoryArticlesRssFeed(), name='mesoblog.feed.rss.categoryFromSlug'),
    url(r'^feed/rss/tag/(?P<tag>[-\w]+)$', TagArticlesRssFeed(), name='mesoblog.feed.rss.tag')
)


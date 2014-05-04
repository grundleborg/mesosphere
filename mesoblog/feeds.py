from django.conf import settings
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

from mesoblog.models import Article, Category

class ArticlesRssFeed(Feed):
    title = settings.SITE_TITLE
    link = reverse_lazy('mesoblog.index')
    description = settings.SITE_DESCRIPTION
    description_template = "mesoblog/feeds/articles-description.html"

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.contents

    def item_link(self, item):
        return reverse('mesoblog.articleFromSlug', args=[item.slug])

class LatestArticlesRssFeed(ArticlesRssFeed):
    def items(self):
        return Article.objects.order_by('-date_published')[:10]

class CategoryArticlesRssFeed(ArticlesRssFeed):
    def get_object(self, request, category_slug = None, category_id = None):
        if category_id is not None:
            return get_object_or_404(Category, id=category_id)
        else:
            return get_object_or_404(Category, slug=category_slug)

    def items(self, obj):
        return Article.objects.filter(categories__id=obj.id).order_by('-date_published')[:10]

class TagArticlesRssFeed(ArticlesRssFeed):
    def get_object(self, request, tag):
        return tag

    def items(self, obj):
        return Article.objects.filter(tags__name__in=[obj]).order_by('-date_published')[:10]

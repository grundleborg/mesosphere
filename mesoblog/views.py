from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from mesoblog.models import Article, Category

# Index view
def index(request):
    articles = Article.objects.all().order_by('-date_published')[:5]
    context = RequestContext(request, {'articles': articles})
    return render(request, 'mesoblog/index.html', context)

# Article view
def article(request, article_id):
    a = get_object_or_404(Article, pk=article_id)
    context = {'article': a}
    return render(request, 'mesoblog/article.html', context)

# Article from Slug view
def articleFromSlug(request, article_slug):
    a = get_object_or_404(Article, slug=article_slug)
    return article(request, a.id)

# Category view
def category(request, category_id):
    articles = Article.objects.filter(categories__id__contains=category_id).order_by('-date_published')[:5]
    context = RequestContext(request, {'articles': articles})
    return render(request, 'mesoblog/index.html', context)

# Category from Slug view
def categoryFromSlug(request, category_slug):
    c = get_object_or_404(Category, slug=category_slug)
    return category(request, c.id)



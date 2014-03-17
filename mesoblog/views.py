from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from mesoblog.models import Article, Category
from mesocore.breadcrumbs import Breadcrumb

# Index view
def index(request):
    articles = Article.objects.all().order_by('-date_published')[:5]

    # Construct Breadcrumbs
    b = [
        Breadcrumb(name="Home"),
        Breadcrumb(name="Blog"),
    ]

    context = RequestContext(request, {'articles': articles, 'breadcrumbs': b,})
    return render(request, 'mesoblog/index.html', context)

# Article view
def article(request, article_id):
    a = get_object_or_404(Article, pk=article_id)

    # Construct Breadcrumbs
    b = [
        Breadcrumb(name="Home"),
        Breadcrumb(name="Blog",url=reverse('mesoblog.views.index')),
        Breadcrumb(name=a.primary_category.name,url=reverse('mesoblog.views.categoryFromSlug',
            args=(a.primary_category.slug,))),
        Breadcrumb(name=a.title)
    ]

    context = {'article': a, 'breadcrumbs': b}
    return render(request, 'mesoblog/article.html', context)

# Article from Slug view
def articleFromSlug(request, article_slug):
    a = get_object_or_404(Article, slug=article_slug)
    return article(request, a.id)

# Category view
def category(request, category_id):
    c = Category.objects.get(id=category_id)
    articles = Article.objects.filter(categories__id__contains=category_id).order_by('-date_published')[:5]

    # Construct Breadcrumbs
    b = [
        Breadcrumb(name="Home"),
        Breadcrumb(name="Blog",url=reverse('mesoblog.views.index')),
        Breadcrumb(name=c.name),
    ]

    context = RequestContext(request, {'articles': articles, 'breadcrumbs': b})
    return render(request, 'mesoblog/index.html', context)

# Category from Slug view
def categoryFromSlug(request, category_slug):
    c = get_object_or_404(Category, slug=category_slug)
    return category(request, c.id)



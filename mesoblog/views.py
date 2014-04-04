from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

import calendar
import pytz

from mesoblog.models import Article, Category, Comment
from mesoblog.forms import CommentForm
from mesocore.breadcrumbs import Breadcrumb

# Load the articles with pagination (reused in several views)
def paginate_articles(articles, page):
    paginator = Paginator(articles, 10)
    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        a = paginator.page(1)
    except EmptyPage:
        a = paginator.page(paginator.num_pages)
    return a

# Index view
def index(request, page=1):
    all_articles = Article.objects.all().order_by('-date_published')
    articles = paginate_articles(all_articles, page)

    # Construct Breadcrumbs
    b = [
        Breadcrumb(name="Home"),
        Breadcrumb(name="Blog"),
    ]

    context = RequestContext(request, {'articles': articles, 'breadcrumbs': b,})
    return render(request, 'mesoblog/index.html', context_instance=context)

# Article view
def article(request, article_id):
    a = get_object_or_404(Article, pk=article_id)
 
    # Handle comment form submission
    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Your comment has been posted successfully.')
            f.save()
            f = CommentForm(instance=Comment(article=a))
        else:
            messages.add_message(request, messages.ERROR, 'Your comment was not posted successfully.')

    else:
        f = CommentForm(instance=Comment(article=a))

    # Construct Breadcrumbs
    b = [
        Breadcrumb(name="Home"),
        Breadcrumb(name="Blog",url=reverse('mesoblog.views.index')),
        Breadcrumb(name=a.primary_category.name,url=reverse('mesoblog.views.categoryFromSlug',
            args=(a.primary_category.slug,))),
        Breadcrumb(name=a.title)
    ]

    context = RequestContext(request, {'article': a, 'breadcrumbs': b, 'comment_form': f})
    return render(request, 'mesoblog/article.html', context_instance=context)

# Article from Slug view
def articleFromSlug(request, article_slug, year=None, month=None, day=None):
    a = get_object_or_404(Article, slug=article_slug)
    return article(request, a.id)

# Category view
def category(request, category_id, page=1):
    c = Category.objects.get(id=category_id)
    all_articles = Article.objects.filter(categories__id__contains=category_id).order_by('-date_published')
    articles = paginate_articles(all_articles, page)

    # Construct Breadcrumbs
    b = [
        Breadcrumb(name="Home"),
        Breadcrumb(name="Blog",url=reverse('mesoblog.views.index')),
        Breadcrumb(name=c.name),
    ]

    context = RequestContext(request, {
            'category': c,
            'articles': articles,
            'breadcrumbs': b,
    })
    return render(request, 'mesoblog/category.html', context_instance=context)

# Category from Slug view
def categoryFromSlug(request, category_slug, page=1):
    c = get_object_or_404(Category, slug=category_slug)
    return category(request, c.id, page)


# Archive view
def archive(request, year, month, page=1):
    all_articles = Article.objects.filter(date_published__year=year,date_published__month=month).order_by('-date_published')
    articles = paginate_articles(all_articles, page)

    # Construct Breadcrumbs
    b = [
        Breadcrumb(name="Home"),
        Breadcrumb(name="Blog",url=reverse('mesoblog.views.index')),
        Breadcrumb(name=calendar.month_name[int(month)]+" "+str(year)),
    ]

    context = RequestContext(request, {
            'month': str(calendar.month_name[int(month)]+" "+str(year)),
            'monthNumber': str(int(month)).zfill(2),
            'year': str(year),
            'articles': articles,
            'breadcrumbs': b,
    })
    return render(request, 'mesoblog/archive.html', context_instance=context)



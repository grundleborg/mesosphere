from django.shortcuts import render, get_object_or_404

from mesoblog.models import Article

# Index view
def index(request):
    articles = Article.objects.all().order_by('-date_published')[:5]
    context = {'articles': articles}
    return render(request, 'mesoblog/index.html', context)

# Article view
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'mesoblog/article.html', context)

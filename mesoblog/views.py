from django.shortcuts import render

from mesoblog.models import Article

# Index view
def index(request):
    articles = Article.objects.all().order_by('-pub_date')[:5]
    context = {'articles': articles}
    return render(request, 'mesoblog/index.html', context)

# Article view
def article(request):
    context = {}
    return render(request, 'mesoblog/article.html', context)

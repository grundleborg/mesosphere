from django.contrib import messages
from django.shortcuts import render
from django.template import RequestContext

from mesoblog.models import Article
from mesocore.breadcrumbs import Breadcrumb

# Create your views here.

def index(request):
    all_articles = Article.objects.all().order_by('-date_published')[:3]
 
    # Construct Breadcrumbs
    context = RequestContext(request, { 'articles': all_articles,})
    return render(request, 'mesohome/index.html', context_instance=context)



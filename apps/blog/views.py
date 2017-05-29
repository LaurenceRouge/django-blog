from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from .models import Category, Article
from .form import ArticleForm
from django.utils import timezone


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    categories = Category.objects.all()
    context = {'latest_article_list': latest_article_list, 'categories': categories}
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail.html', {'article': article})

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles = Article.objects.all()
    return render(request, 'blog/category.html', {'category': category, 'articles': articles})

def write(request):
    if request.user.is_authenticated():
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.pub_date = timezone.now()
            article.save()
            return render(request, 'blog/detail.html', {'article': article})
        else:
            form = ArticleForm()
        return render(request, 'blog/write.html', {'form': form,'form_class': form})
    else:
        return HttpResponse("Gros problemo")

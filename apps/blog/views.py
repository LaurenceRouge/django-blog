from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Category, Article
from .form import ArticleForm
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['latest_article_list'] = Article.objects.order_by('-pub_date')[:5]
        context['categories'] = Category.objects.all()
        return context
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'


class CategoryView(generic.DetailView):
    model = Category
    template_name = 'blog/category.html'

class FormCreate(CreateView):
    form_class = ArticleForm
    template_name = 'blog/write.html'

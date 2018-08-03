from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from blog.models import Article
# Create your views here.

class ArticleListView(TemplateView):
    template_name = "article/index.html"

    def get(self, request, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)

        articles = Article.objects.order_by('-created_at')
        context['articles'] = articles

        return render(self.request, self.template_name, context)

class ArticleView(TemplateView):
    template_name = "article/article.html"

    def get(self, request, *args, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        article = get_object_or_404(Article, pk=context['article_id'])
        context['article'] = article
        return render(self.request, self.template_name, context)
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from collections import OrderedDict

from blog.models import Article

class ArticleListView(TemplateView):
    articles = []

    def get(self, request, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        #articles = Article.objects.order_by('-created_at')
        for article in Article.objects.order_by('-created_at'):
            #category = article.category.
            article_dict = OrderedDict([
                ('id', article.id),
                ('title', article.title),
                ('body', article.body),
                ('category', article.category.name),
                ('created_at', article.created_at.__str__()),
                ('updated_at', article.updated_at.__str__()),
            ])
            self.articles.append(article_dict)
        data = OrderedDict([('articles', self.articles)])
        return render_json_response(request, data)


def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleListView.as_view()),
    path('<int:article_id>', views.ArticleView.as_view()),
]
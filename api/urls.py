from django.urls import path
from api import views

app_name = 'api'

app_name = 'api'
urlpatterns = [
    path('articles/', views.ArticleListView.as_view()), 
]
from django.urls import path
from .views import ArticleCreateView, ArticleListView, ArticlelistByMarketplace, ArticleDetailView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path('article/create/', ArticleCreateView.as_view(), name='article-create'),
    path('article/list/', ArticleListView.as_view(), name='article-list'),
    path('article/list/<int:pk>/', ArticlelistByMarketplace.as_view(), name='article-list-by-marketplace'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]

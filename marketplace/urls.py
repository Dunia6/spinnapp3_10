from django.urls import path
from .views import MarketplaceCreateView, MarketplaceListView, MarketplaceUpdateView, MarketplaceDeleteView, MarketplaceDetailView


urlpatterns = [
    path('marketplaces/', MarketplaceListView.as_view(), name='marketplace-list'),
    path('marketplaces/<int:pk>/', MarketplaceDetailView.as_view(), name='marketplace'),
    path('marketplaces/create/', MarketplaceCreateView.as_view(), name='marketplace-create'),
    path('marketplaces/<int:pk>/update/', MarketplaceUpdateView.as_view(), name='marketplace-update'),
    path('marketplaces/<int:pk>/delete/', MarketplaceDeleteView.as_view(), name='marketplace-delete'),
]

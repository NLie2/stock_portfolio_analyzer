from .views import TradeListView, TradeDetailView
from django.urls import path

# Every request that hits this file will start with /books/
urlpatterns = [
    path('', TradeListView.as_view()), # the full path for this view is /trades/
    path('<int:pk>/', TradeDetailView.as_view()) # full path for this would be /trades/:id/
    
]
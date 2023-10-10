from .views import TradeTableView
from django.urls import path

# Every request that hits this file will start with /books/
urlpatterns = [
    path('<int:pk>/', TradeTableView.as_view()) # full path for this would be /tradestable/:id/
    
]
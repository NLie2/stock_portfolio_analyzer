from .views import NetworthListView, NetworthDetailView
from django.urls import path

# Every request that hits this file will start with /books/
urlpatterns = [
    path('', NetworthListView.as_view()), # the full path for this view is /trades/
    path('<int:pk>/', NetworthDetailView.as_view()) # full path for this would be /trades/:id/
    
]
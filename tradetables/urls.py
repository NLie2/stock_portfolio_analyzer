from .views import TradetableDetailView, TradetableListView
from django.urls import path

# Every request that hits this file will start with /books/
urlpatterns = [
    path('', TradetableListView.as_view()), # full path for this would be /tradestable/
    path('user/<int:pk>/', TradetableDetailView.as_view()), # full path for this would be /tradestable/user/:userid/
    path('<int:pk>/', TradetableDetailView.as_view()) # full path for this would be /tradestable/:id/
]
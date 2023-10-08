from .views import NetworthListView, NetworthDetailView
from django.urls import path

urlpatterns = [
    path('', NetworthListView.as_view()), 
    path('<int:pk>/', NetworthDetailView.as_view())
    
]
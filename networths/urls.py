from .views import NetworthListView, NetworthDetailView, UserNetworthListView
from django.urls import path

urlpatterns = [
    path('', NetworthListView.as_view()), 
    path('<int:pk>/', NetworthDetailView.as_view()),
    path('user/', UserNetworthListView.as_view())
 
]
from django.urls import path
from .views import (
    ThoughtListView,
    ThoughtCreateView,
    ThoughtDetailView,
    ThoughtUpdateView,
    ThoughtDeleteView,
)

urlpatterns = [
    path('home', ThoughtListView.as_view(), name='feeds-home'),
    path('feeds/new/', ThoughtCreateView.as_view(), name='feed-create'),
    path('feeds/detail/<int:pk>/', ThoughtDetailView.as_view(), name='feed-detail'),
    path('feeds/update/<int:pk>/', ThoughtUpdateView.as_view(), name='feed-update'),
    path('feeds/delete/<int:pk>/', ThoughtDeleteView.as_view(), name='feed-delete'),
]

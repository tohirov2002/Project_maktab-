from django.urls import path

from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    NewsListView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
    NewsListVedioView,
    NewsVedioCreateView,
    NewsVedioUpdateView,
    NewsVedioDeleteView
)

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view()),
    path('', NewsListView.as_view()),
    path('create/', NewsCreateView.as_view()),
    path('update/<int:pk>/', NewsUpdateView.as_view()),
    path('delete/<int:pk>/', NewsDeleteView.as_view()),
    path('vedio/', NewsListVedioView.as_view()),
    path('vedio/create/', NewsVedioCreateView.as_view()),
    path('vedio/update/<int:pk>/', NewsVedioUpdateView.as_view()),
    path('vedio/delete/<int:pk>/', NewsVedioDeleteView.as_view())
]
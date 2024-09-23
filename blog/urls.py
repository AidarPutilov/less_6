from django.urls import path
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogArchiveListView,
    toggle_published,
)
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path('blog_list', BlogListView.as_view(), name='blog_list'),
    path('archive_blog_list', BlogArchiveListView.as_view(), name='archive_blog_list'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_published/<int:pk>/', toggle_published, name='toggle_published'),
]
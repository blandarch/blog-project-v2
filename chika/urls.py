from django.urls import path
from .views import (
    ChikaListView, 
    ChikaDetailView,
    ChikaCreateView, 
    ChikaUpdateView, 
    ChikaDeleteView, 
    CommentUpdateView, 
    CommentDeleteView,

)

urlpatterns = [
    path('', ChikaListView.as_view(), name='home'),
    path('post/<int:pk>/', ChikaDetailView.as_view(), name='post_detail'),
    path('post/new/', ChikaCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', ChikaUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', ChikaDeleteView.as_view(), name='post_delete'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]


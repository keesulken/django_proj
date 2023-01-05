from django.urls import path
from .views import *

urlpatterns = [
    (path('', NewsList.as_view(), name='post_list')),
    (path('search/', NewsSearch.as_view(), name='post_search')),
    (path('<int:pk>', NewsDetail.as_view(), name='post_detail')),
    (path('post/create/', NewsCreate.as_view(), name='post_create')),
    (path('post/edit/<int:pk>', NewsEdit.as_view(), name='post_edit')),
    (path('post/delete/<int:pk>', NewsDelete.as_view(), name='post_delete')),
    (path('articles/create/', NewsCreate.as_view(), name='art_create')),
    (path('articles/edit/<int:pk>', NewsEdit.as_view(), name='art_edit')),
    (path('articles/delete/<int:pk>', NewsDelete.as_view(), name='art_delete')),
]
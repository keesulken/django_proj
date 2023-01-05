from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )

from .models import Post
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 2


class NewsSearch(ListView):
    model = Post
    template_name = 'news/news_search.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news_detail'


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if 'post' in self.request.path:
            post.type = 'nw'
        else:
            post.type = 'at'
        return super().form_valid(form)


class NewsEdit(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'post' in self.request.path:
            context['items'] = Post.objects.filter(type='nw')
        else:
            context['items'] = Post.objects.filter(type='at')
        return context


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('post_list')

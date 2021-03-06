from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category)
    return render(request, 'categories.html', {'category': category.title(), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

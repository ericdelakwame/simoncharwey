from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import (
    Post, Comment, 
)
from dashboard.models import (
    Press, About, Work, Teaching
)
from django.views.generic import (
    TemplateView, DetailView
)
from django.views.generic.edit import (
    CreateView, FormView
)
from .forms import CommentForm


class IndexView(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.order_by('-created')[0:5]
        press_entries = Press.objects.order_by('-created')
        teaching_entries = Teaching.objects.order_by('-created')
        about_entries = About.objects.order_by('-created')
        work_entries = Work.objects.order_by('-created')
        context["latest_posts"] = latest_posts
        context["teaching_entries"] = teaching_entries
        context["about_entries"] = about_entries
        context["press_entries"] = press_entries
        context["work_entries"] = work_entries
        
        return context


class PostsView(TemplateView):
    template_name = 'home/posts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.order_by('-created')
        return context
    
    
class PostDetailView(DetailView, FormView):
    template_name = 'home/post_detail.html'
    model = Post
    form_class = CommentForm
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        context["post"] = post
        other_posts = Post.objects.exclude(pk=post.pk)
        context['other_posts'] = other_posts
        return context
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        return reverse('home:post_detail', kwargs={'pk': post.pk})

class TagView(TemplateView):
    template_name = 'home/post_tags.html'
    
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag  = self.kwargs['tag']
        posts = Post.objects.filter(tags__name=tag).prefetch_related('author').order_by('-created')
        context["posts"] = posts
        context['tag'] = tag
        return context

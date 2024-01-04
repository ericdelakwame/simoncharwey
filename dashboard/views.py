from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import (
    TemplateView, DetailView
)

from django.views.generic.edit import (
    UpdateView, DeleteView, FormView, CreateView
)
from home.models import (
    Post, PostImage, PostVideo, Comment,
)
from accounts.models import (
    User, 
)

from .models import (
    Press, Work, Teaching, About
)

from .forms import (
    PressForm, AboutForm, TeachingForm, WorkForm
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin)
from home.forms import (
    CommentForm, PostForm, PostImageForm, PostVideoForm,
    
    )
from django.db.models import Count, Sum


class AdminTestMixin(UserPassesTestMixin, LoginRequiredMixin):
    login_url = '/accounts/login'

    def test_func(self):
        return self.request.user.is_superuser

def site_view(request):
    site_labels = ['Users', 'Posts', 'Comments']
    site_data = []
    users_count = User.objects.values('id').count()
    posts_count = Post.objects.values('id').count()
    comments_count = Comment.objects.values('id').count()
    site_data.append(users_count)
    site_data.append(posts_count)
    site_data.append(comments_count)
    return JsonResponse(data={'data': site_data, 'labels': site_labels})

class IndexView(AdminTestMixin, TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intro'] = 'intro'
        return context

  


class ActivateUser(AdminTestMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        user.activated = True
        user.is_active = True
        user.save()
        context['users'] = User.objects.all()
        context['user'] = user
        return context


class DeactivateUser(AdminTestMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        user.activated = False
        user.is_active = False
        user.save()
        context['users'] = User.objects.all()
        context['user'] = user
        return context


class UsersView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context


class PostsView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.select_related(
            'author').order_by('-created')
        return context


class PostDetailView(LoginRequiredMixin, DetailView, FormView):
    model = Post
    template_name = 'dashboard/index.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        context['post'] = post
        context['comments'] = post.comments.order_by('-created')
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        return reverse('dashboard:post_detail', kwargs={'pk': post.pk})


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'dashboard/forms/post_update_form.html'
    success_url = '/dashboard/posts'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard:posts')
    template_name = 'dashboard/forms/post_delete_form.html'


class AddPostVideo(LoginRequiredMixin, CreateView):
    model = PostVideo
    template_name = 'dashboard/forms/post_video_form.html'
    form_class = PostVideoForm

    def form_valid(self, form):
        video = form.save()
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        post.videos.add(video)
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        return reverse('dashboard:post_detail', kwargs={'pk': post.pk})


class AddPostImage(LoginRequiredMixin, CreateView):
    model = PostImage
    template_name = 'dashboard/forms/post_image_form.html'
    form_class = PostImageForm

    def form_valid(self, form):
        image = form.save()
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        post.images.add(image)
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=pk)
        return reverse('dashboard:post_detail', kwargs={'pk': post.pk})


class NewPost(LoginRequiredMixin, CreateView, FormView):
    login_url = '/accounts/login'
    template_name = 'dashboard/forms/post_form.html'
    form_class = PostForm
    success_url = '/dashboard/posts'
    
    def  form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

class NewPress(AdminTestMixin, CreateView, FormView):
    model = Press
    template_name = 'dashboard/forms/press_form.html'
    success_url = '/dashboard'
    form_class = PressForm
    
    def  form_valid(self, form):
        press = form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    
    
class UpdatePress(AdminTestMixin, UpdateView):
    template_name = 'dashboard/forms/update_press_form.html'
    form_class = PressForm
    success_url = '/dashboard'
    model = Press
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        press = get_object_or_404(Press, pk=pk)
        context["object"] = press
        return context

class DeletePress(AdminTestMixin, DeleteView):
    template_name = 'dashboard/forms/delete_press_form.html'
    success_url = '/dashboard'
    model = Press
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        press = get_object_or_404(Press, pk=pk)
        context["object"] = press
        return context


class AboutEntry(AdminTestMixin, CreateView, FormView):
    model = About
    template_name = 'dashboard/forms/about_form.html'
    success_url = '/dashboard'
    form_class = AboutForm
    
    def  form_valid(self, form):
        about = form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    
    
class UpdateAbout(AdminTestMixin, UpdateView):
    template_name = 'dashboard/forms/update_about_form.html'
    form_class = AboutForm
    success_url = '/dashboard'
    model = About
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        about = get_object_or_404(About, pk=pk)
        context["object"] = about
        return context

class DeleteAbout(AdminTestMixin, DeleteView):
    template_name = 'dashboard/forms/delete_about_form.html'
    success_url = '/dashboard'
    model = Press
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        press = get_object_or_404(Press, pk=pk)
        context["object"] = press
        return context


class WorkEntry(AdminTestMixin, CreateView, FormView):
    model = Work
    template_name = 'dashboard/forms/work_form.html'
    success_url = '/dashboard'
    form_class = WorkForm
    
    def  form_valid(self, form):
        work = form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    
    
class UpdateWork(AdminTestMixin, UpdateView):
    template_name = 'dashboard/forms/update_work_form.html'
    form_class = WorkForm
    success_url = '/dashboard'
    model = Work
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        work = get_object_or_404(Work, pk=pk)
        context["object"] = work
        return context

class DeleteWork(AdminTestMixin, DeleteView):
    template_name = 'dashboard/forms/delete_work_form.html'
    success_url = '/dashboard'
    model = Work
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        work = get_object_or_404(Work, pk=pk)
        context["object"] = work
        return context

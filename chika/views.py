from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .forms import CommentForm
import re


# Create your views here.
class ChikaListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    login_url = 'login'

class ChikaDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.all()
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)
        
        return data
    
    def post(self, request, *args, **kwargs):
        
        new_comment = Comment(
            author=self.request.user,
            comment=request.POST.get('comment'),
            to_chika_post=self.get_object(),
        )
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class ChikaCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChikaUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ChikaDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    fields = ['comment']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        obj = self.get_object()
        regex = re.compile(r'\d+')
        obj_arg = regex.search(str(obj.to_chika_post))
        return reverse_lazy('post_detail', args=[obj_arg.group()])

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        obj = self.get_object()
        regex = re.compile(r'\d+')
        obj_arg = regex.search(str(obj.to_chika_post))
        return reverse_lazy('post_detail', args=[obj_arg.group()])




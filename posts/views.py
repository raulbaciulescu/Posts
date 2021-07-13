from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from posts.models import Post, Comment


class PostList(ListView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = ['image', 'description', 'author']
    success_url = '/'


class CommentForm(forms.Form):
    comment = forms.CharField()

class PostDetail(DetailView):
    model = Post

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                author=request.user,
                post=self.get_object(),
                text=comment_form.cleaned_data['comment']
            )
            comment.save()
        else:
            raise Exception
        return redirect(reverse('posts:detail', args=[self.get_object().id]))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

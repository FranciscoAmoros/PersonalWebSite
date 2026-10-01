from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # lo deja logueado al registrarse
            return redirect(request.POST.get("next") or "blog:post_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        "form": form,
        "next": request.GET.get("next", ""),
    })


def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": post.comments.select_related("author"),
    })


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form, "post": post})
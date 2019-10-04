from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


User = get_user_model()


@login_required
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_list.html', {
        'posts': posts,
        'form': form
    })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user or request.user.is_superuser:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect('post_list')
        else:
            form = PostForm(instance=post)
        return render(request, 'post_edit.html', {'form': form})
    else:
        return HttpResponse(
            'Your user does not have permission to do this action.')


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user or request.user.is_superuser:
        query = Post.objects.get(pk=pk)
        query.delete()
        return redirect('post_list')
    else:
        return HttpResponse(
            'Your user does not have permission to do this action.')

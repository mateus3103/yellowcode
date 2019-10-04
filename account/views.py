from posts.models import Post
from django.db import transaction
from django.utils import timezone
from posts.forms import PostForm
from .forms import UserForm, ProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


User = get_user_model()
users = User.objects.all().select_related('profile')


@login_required
def edit_password(request):
    template_name = 'edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
            return redirect('account')
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def account(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('account')
    else:
        form = PostForm()
    return render(request, 'account.html', {
        'posts': posts,
        'form': form
    })


@login_required
@transaction.atomic
def edit_info(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('account')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_info.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user_model


User = get_user_model()


def create(request):
    template_name = 'create.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('post_list')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def user_login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
            if user is not None:
                return HttpResponse('Invalid account')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

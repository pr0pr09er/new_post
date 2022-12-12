from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from postApp import forms
from .models import Post


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all.html', {'posts': posts})


def add_new(request):
    if request.method == 'POST':
        header = request.POST.get('header')
        content = request.POST.get('content')
        is_publish = request.POST.get('is_publish')
        date = request.POST.get('date')
        if is_publish:
            post = Post.objects.create(header=header, content=content, date=date)
            post.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('<h2>Post not published</h2>')
    else:
        post = forms.PostForm()
        return render(request, 'add_new.html', {'form': post})


def edit(request, id):
    try:
        post = Post.objects.get(id=id)
        if request.method == 'POST':
            post.header = request.POST.get('header')
            post.content = request.POST.get('content')
            post.date = request.POST.get('date')
            post.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'post': post})
    except post.DoesNotExist:
        return HttpResponseNotFound('<h2>Post id not found</h2>')


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect('/')
    except post.DoesNotExist:
        return HttpResponseNotFound('<h2>Post id not found</h2>')

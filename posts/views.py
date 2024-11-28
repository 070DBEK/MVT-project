from django.shortcuts import render
from .models import Post


def task_list(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    if title is not None and content is not None:
        Post.objects.create(title = title,
        content = content
        )
    posts = Post.objects.all()
    ctx = {'posts':posts}
    return render(request, template_name='posts/post-list.html', ctx)
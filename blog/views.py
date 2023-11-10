from django.shortcuts import render

# from django.http import HttpResponse
from .models import Post


def index(request):
    post_list = Post.objects.order_by('created_date')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    context = {'post': Post.objects.get(id=post_id) }
    return render(request, 'blog/detail.html', context)


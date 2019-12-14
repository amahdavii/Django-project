from datetime import datetime
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from django.views.decorators.http import require_http_methods, require_GET, require_safe

from .models import Post
# Create your views here.

@require_http_methods(["GET"])
def index(request):
    latest_posts_list = Post.objects.order_by('-published')[:5]
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return render(request, 'index.html', context)

@require_GET
def detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)

@require_safe
def archive_year(request, year):
    year_archive_posts = get_list_or_404(Post, published__year = year)
    context = {
        'year_archive_posts': year_archive_posts,
    }

    return render(request, 'archive.html', context)
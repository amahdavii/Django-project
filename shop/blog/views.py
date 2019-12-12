from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post
# Create your views here.
def index(request):
    latest_posts_list = Post.objects.order_by('-published')[:5]
    output = ", \n".join([p.slug for p in latest_posts_list])
    return HttpResponse(output)

def detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())
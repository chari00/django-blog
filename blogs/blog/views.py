# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request, 'blog/index.html')


from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

"""def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 2)  # Показывать 10 постов на одной странице
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts_task/post_list.html', context)"""


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    # Получаем выбранный пользователем лимит постов на странице
    limit = request.GET.get('limit', 10)
    paginator = Paginator(posts, int(limit))

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'limit': limit,
    }
    return render(request, 'posts_task/post_list1.html', context)
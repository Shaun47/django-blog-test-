from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.get_page(page)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        posts = paginator.page(paginator.num_pages)

    # sending the page object to index.html
    return render(request, "blog/post/list.html", {
        'page': page,
        'posts': posts
    }
                  )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    page_number = request.GET.get('page')
    return render(request, 'blog/post/detail.html', {'post': post})

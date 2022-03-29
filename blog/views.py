from .models import *
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404



def index(request):
    specialposts = Post.objects.filter(
        is_special=True).order_by('-updated_at')[:4]
    allcats = Category.objects.all().order_by('-order')[:4]
    return render(request, 'blog/index.html', {
        'posts': specialposts,
        'categories': allcats
    })


def post_page(request, pslug):
    the_post = get_object_or_404(Post, slug=pslug)
    category = Category.objects.get(id=the_post.category_id)
    return render(request, 'blog/post.html', {
        'post': the_post,
        'category': category.__str__
    })


def cat_page(request, cat_slug):
    the_cat = get_object_or_404(Category, slug=cat_slug)
    catpost = Category.objects.get(slug=cat_slug)
    category_posts = list(catpost.categories.all())
    return render(request, 'blog/category.html', {
        'cat': the_cat,
        'catposts': category_posts
    })


def pages(request, page):
    basic_options = BlogOptions.objects.all()[0]
    if page == 'about':
        return render(request, 'blog/about.html', {
            'title': 'about us',
            'options': basic_options
        })
    elif page == 'contact':
        return render(request, 'blog/contact.html', {
            'title': 'contact us',
            'options': basic_options
        })
    elif page == 'posts':
        allposts = Post.objects.all()
        return render(request, 'blog/posts.html', {
            'title': 'all posts',
            'posts': allposts
        })
    elif page == 'categories':
        allcats = Category.objects.all()
        return render(request, 'blog/categories.html', {
            'title': 'all categories',
            'categories': allcats

        })
    else:
        raise Http404()

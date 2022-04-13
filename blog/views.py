from webbrowser import get
from .models import *
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .forms import CommentForm
from django.views import View
from django.urls import reverse


# Old Way
# def index(request):
#     specialposts = Post.objects.filter(
#         is_special=True).order_by('-updated_at')[:4]
#     allcats = Category.objects.all().order_by('-order')[:4]
#     return render(request, 'blog/index.html', {
#         'posts': specialposts,
#         'categories': allcats
#     })


class MainPage(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(
            is_special=True).order_by('-updated_at')[:4]
        context['categories'] = Category.objects.all().order_by('-order')[:4]
        return context

# oldway
# def post_page(request, pslug):
#     the_post = get_object_or_404(Post, slug=pslug)
#     category = Category.objects.get(id=the_post.category_id)
#     tags = the_post.posttag.all()
#     return render(request, 'blog/post.html', {
#         'post': the_post,
#         'category': category,
#         'category_name': category.__str__,
#         'tags': tags
#     })


# the way for jus show the post without comment form
# class PostView(DetailView):
#     template_name = 'blog/post.html'
#     model = Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.get(id=self.object.category_id)
#         context['tags'] = self.object.posttag.all()
#         context['comment_form'] = CommentForm()
#         return context


class PostView(View):
    def get(self, request, slug):
        the_post = get_object_or_404(Post, slug=slug)
        category = Category.objects.get(id=the_post.category_id)
        tags = the_post.posttag.all()
        comments = Comment.objects.filter(post=the_post.id, is_active=True).order_by('-created_at')
        context = {
            'post': the_post,
            'category': category,
            'tags': tags,
            'comment_form': CommentForm(),
            'comments': comments,
        }
        return render(request, 'blog/post.html', context)

    def post(self, request, slug):
        formcomment = CommentForm(request.POST)
        the_post = get_object_or_404(Post, slug=slug)
        category = Category.objects.get(id=the_post.category_id)
        tags = the_post.posttag.all()
        comments = Comment.objects.filter(post=the_post.id, is_active=True).order_by('-created_at')

        if formcomment.is_valid():
            comment = formcomment.save(commit=False)
            comment.post = the_post
            comment.save()
            # return HttpResponseRedirect(reverse('post_page', args=[slug]))
            the_post = get_object_or_404(Post, slug=slug)
            category = Category.objects.get(id=the_post.category_id)
            tags = the_post.posttag.all()
            comments = Comment.objects.filter(post=the_post.id, is_active=True).order_by('-created_at')
            context = {
                'post': the_post,
                'category': category,
                'tags': tags,
                'comment_form': CommentForm(),
                'success': 'Thankyou, Your comment After Review by Admin, will display',
                'comments': comments,
            }

            return render(request, 'blog/post.html', context)

        context = {
            'post': the_post,
            'category': category,
            'tags': tags,
            'comment_form': CommentForm,
            'comments': comments,
        }
        return render(request, 'blog/post.html', context)


# oldway
# def cat_page(request, cat_slug):
#     the_cat = get_object_or_404(Category, slug=cat_slug)
#     category_posts = Category.get_category_posts(cat_slug)
#     return render(request, 'blog/category.html', {
#         'cat': the_cat,
#         'catposts': category_posts
#     })


class CategoryPage(DetailView):
    template_name = 'blog/category.html'
    model = Category
    context_object_name = 'cat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["catposts"] = self.object.categories.all()
        return context

# oldway
# def tag_page(request, tag_slug):
#     the_tag = get_object_or_404(Tag, slug=tag_slug)
#     tag_posts = Tag.get_tag_posts(the_tag.id)
#     return render(request, 'blog/tag.html', {
#         'tag': the_tag,
#         'tagposts': tag_posts
#     })


class TagPage(DetailView):
    template_name = 'blog/tag.html'
    model = Tag
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tagposts"] = self.object.tags.all()
        return context


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
    elif page == 'tags':
        alltags = Tag.objects.all()
        return render(request, 'blog/tags.html', {
            'title': 'all Tags',
            'tags': alltags,

        })
    else:
        raise Http404()

from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def post_page(request, slug):
    return HttpResponse(f'This is the {slug} page')


def cat_page(request, cat_slug):
    return HttpResponse(f'This is the {cat_slug} page')


def pages(request, page):
    if page == 'about':
        return render(request, 'blog/about.html', {
            'title': 'about us',
            'text': 'When visitors get to know you and your business better through your about page, \
                     they’ll form a better connection with you. This will make them more likely to read your content, \
                     subscribe to your email list, and become customers.\
                     First Smile Then Continue ... \
                     Experienced Head of SBU(Small Business Unit) in a Software Developing Company \
                     with a demonstrated history of working in the Information Technology & Services industry. \
                     Skilled in Product Management, Project Management, System Analysis, \
                     Scrum Methodology and Knowledge Management. \
                     PhD focused in Management Information Systems and Services from University of Tehran.  '
        })
    elif page == 'contact':
        return render(request, 'blog/contact.html', {
             'title': 'contact us',
             'tell': '09356706868',
             'email': 'info@test.ir',
             'address': 'Tehran, Dr Qarib St., Sahba V., No 17',
             'telegram': 'https://t.me/mohammadisaeedir'
        })
    elif page == 'posts':
        return render(request, 'blog/posts.html', {
             'title': 'All Posts',
             'text': 'This is the contact page'
        })
    elif page == 'categories':
        return HttpResponse('This is the categories page')
    else:
        return HttpResponseNotFound('404')

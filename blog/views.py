import re
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from datetime import date


# --------------------------- Basic Data ----------------------
all_posts = [
    {
        'title': 'python',
        'slug': 'python',
        'updated_at': date(2021, 7, 11),
        'excerpt': 'synatx and basic information',
        'image': 'python.jpg',
        'content': """
            Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.

            Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
        """
    },
    {
        'title': 'Django',
        'slug': 'django',
        'updated_at': date(2021, 10, 12),
        'excerpt': 'offline course',
        'image': 'django.png',
        'content': """
            Django (JANG-goh; sometimes stylized as django)[6] is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern.[7][8] It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit. 

            Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.[9] Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models. 
        """
    },
    {
        'title': 'html5',
        'slug': 'html5',
        'updated_at': date(2019, 8, 11),
        'excerpt': 'synatx and basic information',
        'image': 'html5.png',
        'content': """
            HTML5 is a markup language used for structuring and presenting content on the World Wide Web. It is the fifth and final[3] major HTML version that is a World Wide Web Consortium (W3C) recommendation. The current specification is known as the HTML Living Standard. It is maintained by the Web Hypertext Application Technology Working Group (WHATWG), a consortium of the major browser vendors (Apple, Google, Mozilla, and Microsoft). 

            HTML5 was first released in a public-facing form on 22 January 2008,[2] with a major update and "W3C Recommendation" status in October 2014.[4][5] Its goals were to improve the language with support for the latest multimedia and other new features; to keep the language both easily readable by humans and consistently understood by computers and devices such as web browsers, parsers, etc., without XHTML's rigidity; and to remain backward-compatible with older software. HTML5 is intended to subsume not only HTML 4 but also XHTML 1 and DOM Level 2 HTML.
        """
    },
    {
        'title': 'post',
        'slug': 'post',
        'updated_at': date(2022, 2, 10),
        'excerpt': 'lorem ipsum',
        'image': 'post.jpg',
        'content': """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum qui modi fuga soluta doloremque, reprehenderit fugit explicabo, suscipit earum voluptatem mollitia expedita ratione impedit est nostrum illo unde sit sint.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum qui modi fuga soluta doloremque, reprehenderit fugit explicabo, suscipit earum voluptatem mollitia expedita ratione impedit est nostrum illo unde sit sint.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum qui modi fuga soluta doloremque, reprehenderit fugit explicabo, suscipit earum voluptatem mollitia expedita ratione impedit est nostrum illo unde sit sint.
        """
    },
]


def get_date(post):
    return post['updated_at']


def get_slug(post):
    return post['slug']


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    list_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'posts': list_posts
    })


def post_page(request, slug):
    the_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post.html', {
        'post': the_post
    })


def cat_page(request, cat_slug):
    return render(request, 'blog/category.html', {
        'title': cat_slug,
        'text': f'this is the category of {cat_slug} page'
    })


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
        sorted_posts = sorted(all_posts, key=get_date, reverse=True)
        return render(request, 'blog/posts.html', {
            'posts': sorted_posts
        })
    elif page == 'categories':
        return render(request, 'blog/categories.html', {
            'title': 'all posts',
            'text': 'this is All Categories page'

        })
    else:
        return HttpResponseNotFound('404')

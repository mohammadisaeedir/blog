from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def func(request):
    return HttpResponse('This is the Main Page')


def pages(request, page):
    if page == 'about':
         return HttpResponse('This is the about page')
    elif page == 'contact':
         return HttpResponse('This is the contact page')

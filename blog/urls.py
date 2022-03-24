from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='url_index'),
    path('<page>', views.pages, name='pages'),
    path('posts/<slug:slug>', views.post_page, name='post_page'),
    path('categories/<slug:cat_slug>', views.cat_page, name='cat_page'),
]

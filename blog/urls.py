from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='url_index'),
    path('readlater', views.ReadLater.as_view(), name='read-later'),
    path('<page>', views.pages, name='pages'),
    
    # path('posts/<slug:pslug>', views.post_page, name='post_page'),
    path('posts/<slug:slug>', views.PostView.as_view(), name='post_page'),
    
    # path('categories/<slug:cat_slug>', views.cat_page, name='cat_page'),
    path('categories/<slug:slug>', views.CategoryPage.as_view(), name='cat_page'),
    
    # path('tags/<slug:tag_slug>', views.tag_page, name='tag_page'),
    path('tags/<slug:slug>', views.TagPage.as_view(), name='tag_page'),
]

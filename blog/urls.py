from django.urls import path
from . import views

urlpatterns = [
    path('', views.func, name='url_index'),
    path('<page>', views.pages, name='pages'),
]

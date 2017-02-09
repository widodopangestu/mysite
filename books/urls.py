"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^vsearch/$', views.validate_search),
    url(r'^all-authors/$', views.all_authors),
    url(r'^all-authors-ctx/$', views.all_authors_ctx),
    url(r'^publishers/$', PublisherListView.as_view()),
    url(r'^books/$', BookListView.as_view()),
    url(r'^publishers/(?P<pk>[0-9]+)/$', PublisherDetailView.as_view(), name='publisher-detail'),
    url(r'^authors/(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^apress-books/$', ApressBookList.as_view()),
    url(r'^books-by-publisher/([\w-]+)/$', PublisherBookList.as_view()),
]

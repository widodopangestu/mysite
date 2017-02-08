import datetime
from django import template
from django.template.defaultfilters import stringfilter
from books.models import Book
register = template.Library()

@register.inclusion_tag('link.html', takes_context=True)
def jump_link(context):
    return {
        'link': context['home_link'],
        'title': context['home_title']
    }

@register.inclusion_tag('books_tag.html')
def books_for_author(author):
    books = Book.objects.filter(authors__id=author.id)
    return {'books': books}

@register.inclusion_tag('books_tag_ctx.html', takes_context=True)
def books_for_author_ctx(context, author):
    books = Book.objects.filter(authors__id=author.id)
    return {'books': books, 'username': context['username']}

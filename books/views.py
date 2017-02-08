from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author
# Create your views here.
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_result.html', {'books' : books, 'query': q})
    else:
        return render(request, 'search_form.html', {'error' : True, 'home_link': '/', 'home_title': 'My Home'})

def validate_search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter search term')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_result.html', {'books': books, 'query': q})
    return render(request, 'validate_search.html', {'errors': errors})

def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'all_authors.html', {'authors': authors})

def all_authors_ctx(request):
    authors = Author.objects.all()
    return render(request, 'all_authors_ctx.html', {'authors': authors, 'username': 'Widodo Pangestu'})

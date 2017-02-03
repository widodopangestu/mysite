from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_result.html', {'books' : books, 'query': q})
    else:
        return render(request, 'search_form.html', {'error' : True})

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

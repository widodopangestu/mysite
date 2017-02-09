from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Book, Author, Publisher
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

class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publishers'

class BookListView(ListView):
    model = Book
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'books'

class PublisherDetailView(DetailView):
    #model = Publisher
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()
    def get_context_data(self, **kwargs):
        context = super(PublisherDetailView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context

class AuthorDetailView(DetailView):
    model = Author
    queryset = Author.objects.all()

    def get_object(self):
        object = super(AuthorDetailView, self).get_object()
        object.last_accessed = timezone.now()
        object.save()
        return object

class ApressBookList(ListView):
    context_object_name = 'books'
    queryset = Book.objects.filter(publisher__name='Apress Publishing')
    template_name = 'books/apress_list.html'

class PublisherBookList(ListView):
    context_object_name = 'books'
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, id=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context

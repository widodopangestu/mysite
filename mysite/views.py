from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
import datetime

def home(request):
    return HttpResponse('Home')

def hello(request):
    return HttpResponse('Hello World')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "in %s hours(s), it will be %s." % (offset, dt)
    return HttpResponse(html)

def template_time(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def template2_time(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def render_time(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def include_time(request):
    now = datetime.datetime.now()
    return render(request, 'include_datetime.html', {'current_date': now})

def extends_time(request):
    now = datetime.datetime.now()
    return render(request, 'extends_datetime.html', {'current_date': now})

def extends_hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'extends_hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})

def html_escape(request):
    return render(request, 'html_escape.html', {'name': '<b>Widodo Pangestu</b>'})

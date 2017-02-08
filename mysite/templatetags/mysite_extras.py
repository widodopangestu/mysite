import datetime
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

def cut(value, arg):
    """Remove all values of args from given string"""
    return value.replace(arg, '')

@register.filter(is_safe=True)
@stringfilter
def lower(value):
    """Convert a string into all lowercase"""
    return value.lower()
    
@register.assignment_tag
def get_current_time(format_string):
   return datetime.datetime.now().strftime(format_string)

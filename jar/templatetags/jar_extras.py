from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def upper(value):
    return value.upper()

@register.filter

def format_dollar(value):
    return "${0:.2f}".format(float(value))
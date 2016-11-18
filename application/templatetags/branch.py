from django import template

register = template.Library()

@register.filter
def branch(value):
    string = value.split("/")
    return string[2]
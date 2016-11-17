from django import template

register = template.Library()

@register.filter
def githuburl(value):
    string = value.replace("api.","")
    string = string.replace("repos/", "")
    return string
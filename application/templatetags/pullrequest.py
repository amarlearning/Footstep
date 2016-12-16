from django import template

register = template.Library()

@register.filter
def pullrequest(value):
    string = value.replace("api.","")
    string = string.replace("repos/", "")
    string = string.replace("/commits", "")
    string = string.replace("pulls", "pull")
    return string
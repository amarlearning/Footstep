from django import template

register = template.Library()

@register.filter
def makeurl(value, args):
    string = value.replace("api.","")
    string = string.replace("repos/", "")
    string = string + '/tree/' +str(args)
    return string
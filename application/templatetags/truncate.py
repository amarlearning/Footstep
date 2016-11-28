from django import template

register = template.Library()

@register.filter
def truncate(value):
	length = len(value)
	if length > 50:
		return value[0:50] + "..."
	else:
		return value[0:50]
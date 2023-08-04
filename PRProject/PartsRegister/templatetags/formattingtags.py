from django import template

register = template.Library()


@register.filter
def ashex(value):
    return hex(value)


@register.filter
def prettybool(value):
    return "✔" if value else "✘"


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

from django import template

register = template.Library()

@register.filter
def to_embed(value):
    return value.replace("watch?v=","embed/")
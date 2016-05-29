import math
from django import template

register = template.Library()


@register.filter
def index(list, index):
    return list[int(index)]

@register.filter
def length(list):
    return math.sqrt(len(list)) * 30

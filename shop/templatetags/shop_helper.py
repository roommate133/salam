from django import template
from ..models import Category,GeneralCategory


register=template.Library()


@register.inclusion_tag('includes/stars.html')

def stars(star_count):
    full_starts=int(star_count)
    half_stars=full_starts != star_count
    empty_stars=5-(full_starts+int(half_stars))
    return {
        'full_starts':range(full_starts),
        'half_stars':half_stars,
        'empty_stars':range(empty_stars),
    }
from django import template


register = template.Library()


@register.filter
def mediapath(object_img):
    return f'media/{object_img}'


@register.simple_tag
def mediapath(object_img):
    return f'media/{object_img}'
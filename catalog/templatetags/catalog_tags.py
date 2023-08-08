from django import template


register = template.Library()


@register.filter
def mediapath(object_img):
    return f'/media/{object_img}'


@register.simple_tag
def mediapath(object_img):
    return f'/media/{object_img}'


@register.filter
def id_path(id):
    return f'/card/{id}'


@register.simple_tag
def id_path(id):
    return f'/card/{id}'
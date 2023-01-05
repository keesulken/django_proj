from django import template


register = template.Library()


@register.filter()
def censor(string):
    return string.replace('he', '***')
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdown_safe(value):
    extensions = ["nl2br", "urlize", "fenced_code", "codehilite",]

    return mark_safe(markdown.markdown(value,
                                       extensions,
                                       safe_mode=True,
                                       enable_attributes=False))

@register.filter(is_safe=False)
@stringfilter
def markdown_unsafe(value):
    extensions = ["nl2br", "urlize", "fenced_code", "codehilite",]

    return markdown.markdown(value,
                            extensions,
                            safe_mode=False,
                            enable_attributes=False)



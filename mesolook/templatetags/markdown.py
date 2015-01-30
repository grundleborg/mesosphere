import markdown
import bleach

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

TAGS_SAFE_SUMMARY = [
        'a',
        'abbr',
        'acronym',
        'b',
        'blockquote',
        'code',
        'em',
        'i',
        'li',
        'ol',
        'strong',
        'ul',
        ]

TAGS_UNSAFE_SUMMARY = TAGS_SAFE_SUMMARY
TAGS_UNSAFE = TAGS_SAFE_SUMMARY

# Important Reminder:
# -------------------
# is_safe=True means Django is allowed to escape any HTML added by the function.
# is_safe=False mean Django is *not* allowed to escape any HTML added by the function.

@register.filter(is_safe=False)
@stringfilter
def markdown_safe(value):
    extensions = ["nl2br", "urlize", "fenced_code", "codehilite",]
    return markdown.markdown(value, extensions=extensions, enable_attributes=False)

@register.filter(is_safe=False)
@stringfilter
def markdown_safe_summary(value):
    extensions = ["nl2br", "urlize", "fenced_code", "codehilite",]
    return bleach.clean(
            markdown.markdown(value, extensions=extensions, enable_attributes=False),
            tags=TAGS_SAFE_SUMMARY,
            strip=True)

@register.filter(is_safe=False)
@stringfilter
def markdown_unsafe(value):
    extensions = ["nl2br", "urlize", "fenced_code", "codehilite",]
    return bleach.clean(
            markdown.markdown(value, extensions=extensions, enable_attributes=False),
            tags=TAGS_UNSAFE,
            strip=True)

@register.filter(is_safe=False)
@stringfilter
def markdown_unsafe_summary(value):
    extensions = ["nl2br", "urlize", "fenced_code", "codehilite",]
    return bleach.clean(
            markdown.markdown(value, extensions=extensions, enable_attributes=False),
            tags=TAGS_UNSAFE_SUMMARY,
            strip=True)


from django import template

register = template.Library()

@register.filter(name='subjects_for_stream')
def subjects_for_stream(subjects, stream):
    return subjects.filter(stream=stream)
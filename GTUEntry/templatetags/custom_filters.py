# exam/templatetags/custom_filters.py

from django import template

register = template.Library()

# @register.filter
# def get_post_value(post_data, field_name):
#     return post_data.get(field_name, '')
#
# @register.filter
# def get_default(value, default=''):
#     return value if value is not None else default
#
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')

@register.filter
def get_range(value, arg=0):
    """Returns a list containing range(value). Optionally adds a starting value."""
    return range(arg, value + arg)

@register.filter
def field_name(form, prefix_and_index):
    """Use like form|field_name:"subject_name_1" """
    return form.get(prefix_and_index, "")

@register.filter
def field_name(form, full_field_name):
    """Access a form field dynamically using form['field_name']."""
    try:
        return form[full_field_name]
    except KeyError:
        return ''

@register.filter
def concat_str(prefix, value):
    """Concatenates string + value (used in templates)."""
    return f"{prefix}{value}"
#
# @register.filter
# def get_post_value(post_data, key):
#     return post_data.get(key, '')
#
#
# @register.filter
# def add_str(value, arg):
#     return str(value) + str(arg)
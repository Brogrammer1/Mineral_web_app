from django import template

register = template.Library()


@register.simple_tag
def group_names():
    group = ['Silicates',
                   'Oxides',
                   'Sulfates',
                   'Sulfides',
                   'Carbonates',
                   'Halides',
                   'Sulfosalts',
                   'Phosphates',
                   'Borates',
                   'OrganicMinerals',
                   'Arsenates',
                   'NativeElements',
                   'Other']

    return group


@register.simple_tag
def alphabet():
    return list('abcdefghijklmnopqrstuvwxyz')



from django import template
from datetime import *

register = template.Library()


@register.filter
def format_timedelta(seconds):
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{days}d {hours:02}:{minutes:02}'


@register.filter
def format_bytes(size):
    power = 1024
    n = 0
    power_labels = {0: 'octets', 1: 'Ko', 2: 'Mo', 3: 'Go', 4: 'To'}

    while size > power and n < len(power_labels) - 1:
        size /= power
        n += 1

    return f"{size:.2f} {power_labels[n]}"


@register.filter
def format_datetime(seconds):
    # Définir la date de référence
    reference_date = datetime(1970, 1, 1)

    # Ajouter les secondes à la date de référence
    new_date = reference_date + timedelta(seconds=seconds)

    # Formater la nouvelle date et heure
    formatted_date = new_date.strftime('%d %b %H:%M:%S')

    # Retourner la date formatée
    return formatted_date


@register.filter
def value_pcent(value):
    try:
        value = str(value[2:])
        value = int(value)
    finally:
        pass
    return value


@register.simple_tag
def set_var(value):
    return value


@register.filter
def is_null(value, key):
    return value.get(key) is None


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

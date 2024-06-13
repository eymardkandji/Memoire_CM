from django import template
import datetime

register = template.Library()

@register.filter
def format_timedelta(seconds):
    td = datetime.timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours}:{minutes:02}:{seconds:02}'

@register.filter
def format_bytes(size):
    power = 1024
    n = 0
    power_labels = {0: 'octets', 1: 'Ko', 2: 'Mo', 3: 'Go', 4: 'To'}

    while size > power and n < len(power_labels) - 1:
        size /= power
        n += 1

    return f"{size:.2f} {power_labels[n]}"

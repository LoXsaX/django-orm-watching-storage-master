from django.utils.timezone import localtime, now


def time_delta(visit):
    entered_at = localtime(visit.entered_at)
    if visit.leaved_at:
        delta_time = localtime(visit.leaved_at) - entered_at
    else:
        delta_time = localtime(now()) - entered_at
    return delta_time


def format_time(deltatime):
    quantity = 60
    seconds = deltatime.total_seconds()
    minutes, seconds = divmod(seconds, quantity)
    hours, minutes = divmod(minutes, quantity)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def is_visit_long(delta_time, minutes=60):
    quantity = 60
    seconds = minutes * quantity
    long_visit = delta_time.total_seconds() > seconds
    return long_visit

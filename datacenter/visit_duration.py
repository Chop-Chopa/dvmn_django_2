from django.utils.timezone import localtime, now


SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at) if visit.leaved_at else localtime(now())
    return leaved_at - entered_at


def format_duration(duration):
    total_minutes = int(duration.total_seconds() // SECONDS_IN_MINUTE)
    hours = total_minutes // MINUTES_IN_HOUR
    minutes = total_minutes % MINUTES_IN_HOUR
    return f'{hours}ч {minutes}мин'


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * 60
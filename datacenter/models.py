from django.db import models
from django.utils.timezone import localtime, now


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )



def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at) if visit.leaved_at else localtime(now())
    return leaved_at - entered_at

def format_duration(duration):
    total_minutes = int(duration.total_seconds() // 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f'{hours}ч {minutes}мин'

def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * 60
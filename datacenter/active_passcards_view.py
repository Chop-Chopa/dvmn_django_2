from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import timedelta
from datacenter.models import get_duration, format_duration, is_visit_long
from django.utils.timezone import localtime, now


def active_passcards_view(request):
    unclosed_visits = Visit.objects.filter(leaved_at__isnull=True)

    for visit in unclosed_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        print(f'Зашёл в хранилище, время по Москве:\n{localtime(visit.entered_at)}')
        print(f'Находится в хранилище:\n{formatted_duration}')

    for visit in unclosed_visits:
        print(visit.passcard.owner_name)

    threshold_minutes = 10

    suspicious_visits = []

    all_visits = Visit.objects.all()

    for visit in all_visits:
        if is_visit_long(visit, minutes=threshold_minutes):
            suspicious_visits.append(visit)

    print(f'Визиты дольше {threshold_minutes} мин: {suspicious_visits}')

    example_passcard = Passcard.objects.all()[0]
    example_visits = Visit.objects.filter(passcard=example_passcard)
    print(example_visits)

    active_passcards = Passcard.objects.filter(is_active=True)

    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)

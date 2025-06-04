from datacenter.models import Passcard, Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        visit_info = {
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(visit_info)

    print(f'Визиты для {passcard.owner_name}: {visits}')

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

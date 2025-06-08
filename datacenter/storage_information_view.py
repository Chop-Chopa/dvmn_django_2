from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from visit_duration import get_duration, format_duration

def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in not_leaved:
        entered_at_local = localtime(visit.entered_at)
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': entered_at_local.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

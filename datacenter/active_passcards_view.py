from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import timedelta
from datacenter.models import get_duration, format_duration, is_visit_long
from django.utils.timezone import localtime, now


def active_passcards_view(request):
    active_passcards = Passcard.objects.filter(is_active=True)

    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)

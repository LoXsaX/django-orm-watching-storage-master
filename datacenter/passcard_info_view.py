from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.helper_function import time_delta, format_time, is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        delta_time = time_delta(visit)
        entered_at = localtime(visit.entered_at)
        visit_time = format_time(delta_time)
        is_strange = is_visit_long(delta_time, minutes=60)
        this_passcard_visits.append (
            {
                'entered_at': entered_at,
                'duration': visit_time,
                'is_strange': is_strange
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
        

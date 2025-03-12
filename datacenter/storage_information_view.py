from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.helper_function import time_delta, format_time



def storage_information_view(request):
    lived_person = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in lived_person:
        delta_time = time_delta(visit)
        entered_at = localtime(visit.entered_at)
        visit_time = format_time(delta_time)
        visite_person_name = visit.passcard
        non_closed_visits.append (
            {
                'who_entered': visite_person_name,
                'entered_at': entered_at,
                'duration': visit_time,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits, 
    }
    return render(request, 'storage_information.html', context)

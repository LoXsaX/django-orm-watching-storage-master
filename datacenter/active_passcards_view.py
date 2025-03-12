from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):

    is_active_passcard = Passcard.objects.filter(is_active = True)
    context = {
        'active_passcards': is_active_passcard,  
    }
    return render(request, 'active_passcards.html', context)

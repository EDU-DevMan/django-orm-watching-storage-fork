from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.duration_date import get_duration
from datacenter.duration_date import format_duration
from datacenter.duration_date import is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects.filter(passcode=passcode))
    this_passcard_visits = []

    for visit in Visit.objects.all().filter(passcard=passcard):
        duration = get_duration(visit)
        this_passcard_visits.append({
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
                'is_strange': (is_visit_long(duration))
            }),

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)

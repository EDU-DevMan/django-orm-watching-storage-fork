from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.duration_date import DurationDate


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects.filter(passcode=passcode))
    this_passcard_visits = []

    for visit in Visit.objects.all().filter(passcard=passcard):
        duration = DurationDate.get_duration(visit)
        this_passcard_visits.append({
                'entered_at': visit.entered_at,
                'duration': DurationDate.format_duration(duration.seconds),
                'is_strange': (DurationDate.is_visit_long(
                   DurationDate.get_duration(visit).seconds)
                    )
            }),

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)

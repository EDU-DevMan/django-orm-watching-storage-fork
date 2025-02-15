from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects.filter(passcode=passcode))
    this_passcard_visits = []

    for visit in Visit.objects.all().filter(passcard=passcard):
        duration = Visit.get_duration(visit)
        this_passcard_visits.append({
                'entered_at': visit.entered_at,
                'duration': Visit.format_duration(duration.seconds),
                'is_strange': (Visit.is_visit_long(
                    Visit.get_duration(visit).seconds)
                    )
            }),

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)

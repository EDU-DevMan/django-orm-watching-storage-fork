from datacenter.models import Visit
from django.shortcuts import render

from datacenter.duration_date import get_duration
from datacenter.duration_date import format_duration
from datacenter.duration_date import is_visit_long


def storage_information_view(request):
    visits = Visit.objects.all().filter(leaved_at=None)
    non_closed_visits = []

    for i in range(len(visits)):
        duration = get_duration(visits[i])
        non_closed_visits.append({
            'who_entered': visits[i].passcard,
            'entered_at': visits[i].created_at,
            'duration': format_duration(duration),
            'is_strange': (is_visit_long(duration))
            })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)

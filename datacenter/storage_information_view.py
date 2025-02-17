from datacenter.models import Visit
from django.shortcuts import render

from datacenter.duration_date import DurationDate


def storage_information_view(request):
    visits = Visit.objects.all().filter(leaved_at=None)
    non_closed_visits = []

    for i in range(len(visits)):
        duration = DurationDate.get_duration(visits[i])
        non_closed_visits.append({
            'who_entered': visits[i].passcard,
            'entered_at': visits[i].created_at,
            'duration': DurationDate.format_duration(duration.seconds),
            'is_strange': (DurationDate.is_visit_long(
                DurationDate.get_duration(visits[i]).seconds)
                    )
            })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)

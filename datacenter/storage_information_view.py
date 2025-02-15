from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.all().filter(leaved_at=None)
    non_closed_visits = []

    for i in range(len(visits)):
        duration = Visit.get_duration(visits[i])
        non_closed_visits.append({
            'who_entered': visits[i].passcard,
            'entered_at': visits[i].created_at,
            'duration': Visit.format_duration(duration.seconds),
            'is_strange': (Visit.is_visit_long(
                Visit.get_duration(visits[i]).seconds)
                    )
            })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)

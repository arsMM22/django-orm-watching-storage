from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.help_function import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    for visit in not_leaved_visits:
        duration = get_duration(visit)
        entered_local_time = localtime(visit.entered_at)
        visit_time = format_duration(duration)
        person = visit.passcard
        long_visit = is_visit_long(duration)
        non_closed_visits.append({
            'who_entered': person,
            'entered_at': entered_local_time,
            'duration': visit_time,
             'is_strange': long_visit
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

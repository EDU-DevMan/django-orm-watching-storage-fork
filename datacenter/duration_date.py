from datetime import timedelta
from django.utils.timezone import localtime


class DurationDate:
    def is_visit_long(visit, minutes=60):
        check_time = (visit/60 > minutes)

        return check_time

    def get_duration(visit):
        time_entered = localtime(visit.entered_at)
        time_leaved = localtime(visit.leaved_at)
        duration = time_leaved - time_entered

        return duration

    def format_duration(duration):
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)

        return f'{hours}ч {minutes}мин'

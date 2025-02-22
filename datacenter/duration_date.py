from django.utils.timezone import localtime


HOURS_CONVERTING = 3600
MINUTES_CONVERTING = 60
class DurationDate:
    def is_visit_long(visit, minutes=MINUTES_CONVERTING):
        check_time = (visit/MINUTES_CONVERTING > minutes)

        return check_time

    def get_duration(visit):
        time_entered = localtime(visit.entered_at)
        time_leaved = localtime(visit.leaved_at)
        duration = time_leaved - time_entered

        return duration.total_seconds()

    def format_duration(duration):
        hours = int(duration // HOURS_CONVERTING)
        minutes = int((duration % HOURS_CONVERTING) // MINUTES_CONVERTING)

        return f'{hours}ч {minutes}мин'

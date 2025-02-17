from datetime import timedelta
from django.utils.timezone import localtime


class DurationDate():
    def is_visit_long(visit, minutes=60):
        if visit / 60 > minutes:
            return True

        return False

    def get_duration(visit):
        time_entered = localtime(visit.entered_at).replace(tzinfo=None)
        time_leaved = localtime(visit.leaved_at).replace(tzinfo=None)
        duration = time_leaved - time_entered

        return duration

    def format_duration(duration):
        string_time = timedelta(seconds=round(duration))

        return string_time

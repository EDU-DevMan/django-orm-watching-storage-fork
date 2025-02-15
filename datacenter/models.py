from django.db import models

from datetime import datetime, timedelta
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def is_visit_long(visit, minutes=60):
        if visit / 60 > minutes:
            return True

        return False

    def get_duration(visit):
        time_now = datetime.now()
        time_then = localtime(visit.entered_at).replace(tzinfo=None)
        duration = time_now - time_then

        return duration

    def format_duration(duration):
        string_time = timedelta(seconds=round(duration))

        return string_time

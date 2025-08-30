
from django.utils.timezone import localtime
from django.utils import timezone

def get_duration(visit):
  if visit.leaved_at:
      delta = localtime(visit.leaved_at) - localtime(visit.entered_at)
  else:
      date_now = localtime(timezone.now())
      delta = date_now - localtime(visit.entered_at) 
  return delta


def format_duration(duration):
  seconds_in_hour = 3600
  seconds_in_minute = 60
  total_seconds = int(duration.total_seconds())
  hours = total_seconds // seconds_in_hour
  minutes = (total_seconds % seconds_in_hour) // seconds_in_minute
  seconds = total_seconds % seconds_in_minute
  return f"{hours}:{minutes}:{seconds}"


def is_visit_long(duration, time_limit=10):
  seconds = time_limit*60
  long_visit = duration.total_seconds()>seconds
  return long_visit

import django_filters
from .models import *

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['course_code', 'subject_title']

class SeminarFilter(django_filters.FilterSet):
    class Meta:
        model = Seminar
        fields = ['first_name', 'last_name']

class WorkshopFilter(django_filters.FilterSet):
    class Meta:
        model = Workshop
        fields = ['first_name', 'last_name', 'subject_handled']

class ScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = Schedule
        fields = ['date_schedule', 'time_schedule', 'subject']

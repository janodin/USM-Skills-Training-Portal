import django_filters
from .models import *

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['course_code', 'subject_title']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']

class FacultyFilter(django_filters.FilterSet):
    class Meta:
        model = Faculty
        fields = ['first_name', 'last_name', 'subject_handled']

class ScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = Schedule
        fields = ['date_schedule', 'time_schedule', 'subject']

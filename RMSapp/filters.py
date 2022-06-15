import django_filters
from .models import *

class SeminarFilter(django_filters.FilterSet):
    class Meta:
        model = Seminar
        fields = ['title', 'conducted']

class WorkshopFilter(django_filters.FilterSet):
    class Meta:
        model = Workshop
        fields = ['first_name', 'last_name', 'subject_handled']


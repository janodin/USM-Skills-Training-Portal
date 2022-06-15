from django.db import models


# Create your models here.

class Course(models.Model):
    class Meta:
        verbose_name_plural = 'Course'

    course_code = models.CharField(max_length=200, null=False, blank=False)
    subject_title = models.CharField(max_length=200, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.subject_title


class Student(models.Model):
    class Meta:
        verbose_name_plural = 'Student'

    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return name


class Faculty(models.Model):
    class Meta:
        verbose_name_plural = 'Faculty'

    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    subject_handled = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return name


class Schedule(models.Model):
    class Meta:
        verbose_name_plural = 'Schedule'

    date_schedule = models.DateField(max_length=200, null=False, blank=False)
    time_schedule = models.TimeField(max_length=200, null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.subject

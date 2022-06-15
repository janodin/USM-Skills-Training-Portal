from django.db import models


# Create your models here.

class Seminar(models.Model):
    class Meta:
        verbose_name_plural = 'Seminar'

    title = models.CharField(max_length=200, null=False, blank=False)
    date_started = models.CharField(max_length=200, null=False, blank=False)
    date_ended = models.CharField(max_length=200, null=False, blank=False)
    time_duration = models.CharField(max_length=200, null=False, blank=False)
    seminar_type = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    conducted = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        name = self.title + ' ' + self.conducted
        return name


class Workshop(models.Model):
    class Meta:
        verbose_name_plural = 'Workshop'

    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    subject_handled = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return name


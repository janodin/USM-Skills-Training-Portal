from django.shortcuts import render, redirect
from django.contrib import messages
from .filters import *


# Create your views here.


def homePage(request):
    courses_count = Course.objects.all().count()
    seminars_count = Seminar.objects.all().count()
    workshops_count = Workshop.objects.all().count()
    schedules_count = Schedule.objects.all().count()

    context = {
        'courses_count': courses_count,
        'seminars_count': seminars_count,
        'workshops_count': workshops_count,
        'schedules_count': schedules_count,
    }
    return render(request, 'home.html', context)


def addCourse(request):
    if request.method == 'POST':
        course_code = request.POST['course_code']
        subject_title = request.POST['subject_title']
        saveCourse = Course(course_code=course_code, subject_title=subject_title)
        saveCourse.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_course.html')


def addSeminar(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        saveSeminar = Seminar(first_name=first_name, last_name=last_name)
        saveSeminar.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_seminar.html')


def addWorkshop(request):
    subjectOptions = Course.objects.all()

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        subject_handled = request.POST['subject_handled']
        saveWorkshop = Workshop(first_name=first_name, last_name=last_name, subject_handled=subject_handled)
        saveWorkshop.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_workshop.html', {'subjectOptions': subjectOptions})


def addSchedule(request):
    subjectOptions = Course.objects.all()

    if request.method == 'POST':
        date_schedule = request.POST['date_schedule']
        time_schedule = request.POST['time_schedule']
        subject = request.POST['subject']
        saveSchedule = Schedule(date_schedule=date_schedule, time_schedule=time_schedule, subject=subject)
        saveSchedule.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_schedule.html', {'subjectOptions': subjectOptions})


def viewCourse(request):
    courses = Course.objects.all()
    courseFilter = CourseFilter(request.GET, queryset=courses)
    courses = courseFilter.qs

    context = {
        'courses': courses,
        'courseFilter': courseFilter
    }
    return render(request, 'view_course.html', context)


def viewSeminar(request):
    seminars = Seminar.objects.all()
    seminarFilter = SeminarFilter(request.GET, queryset=seminars)
    seminars = seminarFilter.qs

    context = {
        'seminars': seminars,
        'seminarFilter': seminarFilter
    }
    return render(request, 'view_seminar.html', context)


def viewWorkshop(request):
    faculties = Workshop.objects.all()
    workshopFilter = WorkshopFilter(request.GET, queryset=faculties)
    workshops = workshopFilter.qs

    context = {
        'workshops': workshops,
        'workshopFilter': workshopFilter
    }
    return render(request, 'view_workshop.html', context)


def viewSchedule(request):
    schedules = Schedule.objects.all()
    scheduleFilter = ScheduleFilter(request.GET, queryset=schedules)
    schedules = scheduleFilter.qs

    context = {
        'schedules': schedules,
        'scheduleFilter': scheduleFilter
    }
    return render(request, 'view_schedule.html', context)


def editCourse(request, courseId):
    courseItem = Course.objects.get(id=courseId)
    return render(request, 'edit_course.html', {'courseItem': courseItem})


def editSeminar(request, seminarId):
    seminarItem = Seminar.objects.get(id=seminarId)
    return render(request, 'edit_seminar.html', {'seminarItem': seminarItem})


def editWorkshop(request, workshopId):
    subjectOptions = Course.objects.all()
    workshopItem = Workshop.objects.get(id=workshopId)

    context = {
        'workshopItem': workshopItem,
        'subjectOptions': subjectOptions
    }
    return render(request, 'edit_workshop.html', context)


def editSchedule(request, scheduleId):
    subjectOptions = Course.objects.all()
    scheduleItem = Schedule.objects.get(id=scheduleId)

    context = {
        'scheduleItem': scheduleItem,
        'subjectOptions': subjectOptions,
    }
    return render(request, 'edit_schedule.html', context)


def updateCourse(request, courseId):
    courseItem = Course.objects.get(id=courseId)
    courseItem.course_code = request.POST['course_code']
    courseItem.subject_title = request.POST['subject_title']
    courseItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewCourse)


def updateSeminar(request, seminarId):
    seminarItem = Seminar.objects.get(id=seminarId)
    seminarItem.first_name = request.POST['f_name']
    seminarItem.last_name = request.POST['l_name']
    seminarItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewSeminar)


def updateWorkshop(request, workshopId):
    workshopItem = Workshop.objects.get(id=workshopId)
    workshopItem.first_name = request.POST['first_name']
    workshopItem.last_name = request.POST['last_name']
    workshopItem.subject_handled = request.POST['subject_handled']
    workshopItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewWorkshop)


def updateSchedule(request, scheduleId):
    scheduleItem = Schedule.objects.get(id=scheduleId)
    scheduleItem.date_schedule = request.POST['date_schedule']
    scheduleItem.time_schedule = request.POST['time_schedule']
    scheduleItem.subject = request.POST['subject']
    scheduleItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewSchedule)


def deleteCourse(request, courseId):
    courseItem = Course.objects.get(id=courseId)
    courseItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewCourse)


def deleteSeminar(request, seminarId):
    seminarItem = Seminar.objects.get(id=seminarId)
    seminarItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewSeminar)


def deleteWorkshop(request, workshopId):
    workshopItem = Workshop.objects.get(id=workshopId)
    workshopItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewWorkshop)


def deleteSchedule(request, scheduleId):
    scheduleItem = Schedule.objects.get(id=scheduleId)
    scheduleItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewSchedule)

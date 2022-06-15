from django.shortcuts import render, redirect
from django.contrib import messages
from .filters import *


# Create your views here.


def homePage(request):
    seminars_count = Seminar.objects.all().count()
    workshops_count = Workshop.objects.all().count()

    context = {
        'seminars_count': seminars_count,
        'workshops_count': workshops_count,
    }
    return render(request, 'home.html', context)


def addSeminar(request):
    if request.method == 'POST':
        title = request.POST['title']
        address = request.POST['address']
        conducted = request.POST['conducted']
        date_started = request.POST['date_started']
        date_ended = request.POST['date_ended']
        time_duration = request.POST['time_duration']
        seminar_type = request.POST['seminar_type']

        saveSeminar = Seminar(title=title, address=address, conducted=conducted, date_started=date_started, date_ended=date_ended, time_duration=time_duration, seminar_type=seminar_type)
        saveSeminar.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_seminar.html')


def addWorkshop(request):
    if request.method == 'POST':
        title = request.POST['title']
        address = request.POST['address']
        conducted = request.POST['conducted']
        date_started = request.POST['date_started']
        date_ended = request.POST['date_ended']
        time_duration = request.POST['time_duration']
        seminar_type = request.POST['seminar_type']
        saveWorkshop = Workshop(title=title, address=address, conducted=conducted, date_started=date_started, date_ended=date_ended, time_duration=time_duration, seminar_type=seminar_type)
        saveWorkshop.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_workshop.html', )


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


def editSeminar(request, seminarId):
    seminarItem = Seminar.objects.get(id=seminarId)
    return render(request, 'edit_seminar.html', {'seminarItem': seminarItem})


def editWorkshop(request, workshopId):
    workshopItem = Workshop.objects.get(id=workshopId)

    context = {
        'workshopItem': workshopItem,
    }
    return render(request, 'edit_workshop.html', context)


def updateSeminar(request, seminarId):
    seminarItem = Seminar.objects.get(id=seminarId)
    seminarItem.title = request.POST['title']
    seminarItem.address = request.POST['address']
    seminarItem.conducted = request.POST['conducted']
    seminarItem.date_started = request.POST['date_started']
    seminarItem.date_ended = request.POST['date_ended']
    seminarItem.time_duration = request.POST['time_duration']
    seminarItem.seminar_type = request.POST['seminar_type']
    seminarItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewSeminar)


def updateWorkshop(request, workshopId):
    workshopItem = Workshop.objects.get(id=workshopId)
    workshopItem.title = request.POST['title']
    workshopItem.address = request.POST['address']
    workshopItem.conducted = request.POST['conducted']
    workshopItem.date_started = request.POST['date_started']
    workshopItem.date_ended = request.POST['date_ended']
    workshopItem.time_duration = request.POST['time_duration']
    workshopItem.seminar_type = request.POST['seminar_type']
    workshopItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewWorkshop)


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

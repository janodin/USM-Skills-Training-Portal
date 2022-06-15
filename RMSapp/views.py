from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from .filters import *



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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        saveSeminar = Seminar(first_name=first_name, last_name=last_name)
        saveSeminar.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_seminar.html')


def addWorkshop(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        subject_handled = request.POST['subject_handled']
        saveWorkshop = Workshop(first_name=first_name, last_name=last_name, subject_handled=subject_handled)
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



class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'register.html', context)

                user = User.objects.create_user(username=username, email=email )
                user.set_password(password)
                user.save()

                messages.success(request, 'you have successfully created an account')
                return render(request, 'login.html', context)


class LoginView(View):
        def get(self, request):
            return render(request, 'login.html')

        def post(self, request):

            username = request.POST['username']
            password = request.POST['password']

            if username and password:
                user = auth.authenticate(username=username, password=password)

                if user:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' + user.username + ' you are now logged in')
                return redirect('home')

            messages.error(
                request, 'Please fill all fields')
            return render(request, 'login.html')

class ProfileView(View):
    def get (self, request):
        return render(request, 'profile.html')

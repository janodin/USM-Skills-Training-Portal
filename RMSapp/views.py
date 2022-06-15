from django.shortcuts import render, redirect
from django.contrib import messages
from .filters import *


# Create your views here.


def homePage(request):
    courses_count = Course.objects.all().count()
    students_count = Student.objects.all().count()
    faculties_count = Faculty.objects.all().count()
    schedules_count = Schedule.objects.all().count()

    context = {
        'courses_count': courses_count,
        'students_count': students_count,
        'faculties_count': faculties_count,
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


def addStudent(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        saveStudent = Student(first_name=first_name, last_name=last_name)
        saveStudent.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_student.html')


def addFaculty(request):
    subjectOptions = Course.objects.all()

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        subject_handled = request.POST['subject_handled']
        saveFaculty = Faculty(first_name=first_name, last_name=last_name, subject_handled=subject_handled)
        saveFaculty.save()
        messages.info(request, 'Added Successfully!')

    return render(request, 'add_faculty.html', {'subjectOptions': subjectOptions})


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


def viewStudent(request):
    students = Student.objects.all()
    studentFilter = StudentFilter(request.GET, queryset=students)
    students = studentFilter.qs

    context = {
        'students': students,
        'studentFilter': studentFilter
    }
    return render(request, 'view_student.html', context)


def viewFaculty(request):
    faculties = Faculty.objects.all()
    facultyFilter = FacultyFilter(request.GET, queryset=faculties)
    faculties = facultyFilter.qs

    context = {
        'faculties': faculties,
        'facultyFilter': facultyFilter
    }
    return render(request, 'view_faculty.html', context)


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


def editStudent(request, studentId):
    studentItem = Student.objects.get(id=studentId)
    return render(request, 'edit_student.html', {'studentItem': studentItem})


def editFaculty(request, facultyId):
    subjectOptions = Course.objects.all()
    facultyItem = Faculty.objects.get(id=facultyId)

    context = {
        'facultyItem': facultyItem,
        'subjectOptions': subjectOptions
    }
    return render(request, 'edit_faculty.html', context)


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


def updateStudent(request, studentId):
    studentItem = Student.objects.get(id=studentId)
    studentItem.first_name = request.POST['f_name']
    studentItem.last_name = request.POST['l_name']
    studentItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewStudent)


def updateFaculty(request, facultyId):
    facultyItem = Faculty.objects.get(id=facultyId)
    facultyItem.first_name = request.POST['first_name']
    facultyItem.last_name = request.POST['last_name']
    facultyItem.subject_handled = request.POST['subject_handled']
    facultyItem.save()
    messages.info(request, 'Updated Successfully!')

    return redirect(viewFaculty)


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


def deleteStudent(request, studentId):
    studentItem = Student.objects.get(id=studentId)
    studentItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewStudent)


def deleteFaculty(request, facultyId):
    facultyItem = Faculty.objects.get(id=facultyId)
    facultyItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewFaculty)


def deleteSchedule(request, scheduleId):
    scheduleItem = Schedule.objects.get(id=scheduleId)
    scheduleItem.delete()
    messages.info(request, 'Deleted Successfully!')

    return redirect(viewSchedule)

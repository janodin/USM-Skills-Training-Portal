from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('addCourse/', views.addCourse, name='add_course'),
    path('addStudent/', views.addStudent, name='add_student'),
    path('addFaculty/', views.addFaculty, name='add_faculty'),
    path('addSchedule/', views.addSchedule, name='add_schedule'),
    path('viewCourse/', views.viewCourse, name='view_course'),
    path('viewStudent/', views.viewStudent, name='view_student'),
    path('viewFaculty/', views.viewFaculty, name='view_faculty'),
    path('viewSchedule/', views.viewSchedule, name='view_schedule'),
    path('editCourse/<int:courseId>/', views.editCourse, name='edit_course'),
    path('editStudent/<int:studentId>/', views.editStudent, name='edit_student'),
    path('editFaculty/<int:facultyId>/', views.editFaculty, name='edit_faculty'),
    path('editSchedule/<int:scheduleId>/', views.editSchedule, name='edit_schedule'),
    path('updateCourse/<int:courseId>/', views.updateCourse, name='update_course'),
    path('updateStudent/<int:studentId>/', views.updateStudent, name='update_student'),
    path('updateFaculty/<int:facultyId>/', views.updateFaculty, name='update_faculty'),
    path('updateSchedule/<int:scheduleId>/', views.updateSchedule, name='update_schedule'),
    path('deleteCourse/<int:courseId>/', views.deleteCourse, name='delete_course'),
    path('deleteStudent/<int:studentId>/', views.deleteStudent, name='delete_student'),
    path('deleteFaculty/<int:facultyId>/', views.deleteFaculty, name='delete_faculty'),
    path('deleteSchedule/<int:scheduleId>/', views.deleteSchedule, name='delete_schedule'),

]

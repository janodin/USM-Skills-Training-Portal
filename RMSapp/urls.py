from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('addCourse/', views.addCourse, name='add_course'),
    path('addSeminar/', views.addSeminar, name='add_seminar'),
    path('addWorkshop/', views.addWorkshop, name='add_workshop'),
    path('addSchedule/', views.addSchedule, name='add_schedule'),
    path('viewCourse/', views.viewCourse, name='view_course'),
    path('viewSeminar/', views.viewSeminar, name='view_seminar'),
    path('viewWorkshop/', views.viewWorkshop, name='view_workshop'),
    path('viewSchedule/', views.viewSchedule, name='view_schedule'),
    path('editCourse/<int:courseId>/', views.editCourse, name='edit_course'),
    path('editSeminar/<int:seminarId>/', views.editSeminar, name='edit_seminar'),
    path('editWorkshop/<int:workshopId>/', views.editWorkshop, name='edit_workshop'),
    path('editSchedule/<int:scheduleId>/', views.editSchedule, name='edit_schedule'),
    path('updateCourse/<int:courseId>/', views.updateCourse, name='update_course'),
    path('updateSeminar/<int:seminarId>/', views.updateSeminar, name='update_seminar'),
    path('updateWorkshop/<int:workshopId>/', views.updateWorkshop, name='update_workshop'),
    path('updateSchedule/<int:scheduleId>/', views.updateSchedule, name='update_schedule'),
    path('deleteCourse/<int:courseId>/', views.deleteCourse, name='delete_course'),
    path('deleteSeminar/<int:seminarId>/', views.deleteSeminar, name='delete_seminar'),
    path('deleteWorkshop/<int:workshopId>/', views.deleteWorkshop, name='delete_workshop'),
    path('deleteSchedule/<int:scheduleId>/', views.deleteSchedule, name='delete_schedule'),

]

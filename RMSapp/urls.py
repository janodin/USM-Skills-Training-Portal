from django.urls import path
from . import views
from .views import LoginView, RegistrationView, ProfileView

urlpatterns = [
    path('', views.homePage, name='home'),
    path('register', RegistrationView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile', ProfileView.as_view(), name="profile"),
    path('addSeminar/', views.addSeminar, name='add_seminar'),
    path('addWorkshop/', views.addWorkshop, name='add_workshop'),
    path('viewSeminar/', views.viewSeminar, name='view_seminar'),
    path('viewWorkshop/', views.viewWorkshop, name='view_workshop'),
    path('editSeminar/<int:seminarId>/', views.editSeminar, name='edit_seminar'),
    path('editWorkshop/<int:workshopId>/', views.editWorkshop, name='edit_workshop'),
    path('updateSeminar/<int:seminarId>/', views.updateSeminar, name='update_seminar'),
    path('updateWorkshop/<int:workshopId>/', views.updateWorkshop, name='update_workshop'),
    path('deleteSeminar/<int:seminarId>/', views.deleteSeminar, name='delete_seminar'),
    path('deleteWorkshop/<int:workshopId>/', views.deleteWorkshop, name='delete_workshop'),

]

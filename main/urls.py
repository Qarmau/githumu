
# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('administration/', views.administration, name='administration'),
    path('teaching-staff/', views.teaching_staff, name='teaching_staff'),
    path('achievements/', views.achievements, name='achievements'),
    path('holiday-assignments/', views.holiday_assignments, name='holiday_assignments'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/application-success/', views.application_success, name='application_success'),
]
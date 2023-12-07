from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('job-listing/', views.job_listing, name='job-listing'),
    path('job-details/<int:pk>/',views.job_details, name='job-details'),


    path('about/', views.about, name='about'),
    path('undermaintenance/', views.error, name='undermaintenance'),
    path('contact/', views.contact, name='contact'),



    
]





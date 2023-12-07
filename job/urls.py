from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job , name="create-job"),
    path('update-job/<int:pk>/',views.update_job, name='update-job'),
    path('manage-jobs/', views.manage_jobs, name='manage-job'),
    path('apply-job/<int:pk>/', views.apply_job, name='apply-job'),
    path('all-applicants/<int:pk>/', views.all_applicants, name='all-applicants'),
    path('applied-jobs/',views.applied_jobs, name='applied-jobs')
]

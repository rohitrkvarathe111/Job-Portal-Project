from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .form import CustomSetPasswordForm



urlpatterns = [
    path('register-applicant/', views.register_applicant, name='register-applicant'),
    path('register-recruiter/', views.register_recruiter, name='register-recruiter'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),



   
    path('all-users/', views.all_users, name='all-users'),
    path('admin-view/', views.admin_view, name='admin-view'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete-user'),



    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/resetpassword.html"), name='reset_password'),

    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(
            template_name='users/resetpassword.html',
            extra_context={'message': 'Password reset link has been sent to your email.Please create a new password through the link.'}
    ), name='password_reset_done'),


    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/newpassword.html',
        form_class=CustomSetPasswordForm,
    ), name='password_reset_confirm'),


    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/newpassword.html',
        extra_context={'message': '  Your password has been changed successfully. Please '}
    ), name='password_reset_complete'),
    
]





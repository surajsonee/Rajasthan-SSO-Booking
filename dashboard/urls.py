"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from users import views
from sso_user.views import sso_register, remove_from_sso
from visitor.views import visitor_registration, add_visitor, edit_visitor, remove_visitor
from booking.views import booking_process, submitted_visitor_report
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('change_password/', views.change_password, name="change_password"),
    path('profile/', views.profile, name="profile"),
    path('sso_user_register/', sso_register, name="sso_register"),
    path('sso_remove/<int:id>',remove_from_sso, name="remove_from_sso"),
    path('visitor_registration/',visitor_registration, name="visitor_registration"),
    path('add_visitor/',add_visitor, name="add_visitor"),
    path('edit_visitor/<int:id>',edit_visitor, name="edit_visitor"),
    path('remove_visitor/<int:id>',remove_visitor, name="remove_from_visitor"),
    path('booking_process/',booking_process, name="booking_process"),
    path('submitted_visitor_report/',submitted_visitor_report, name="submitted_visitor_report"),
    path('logout/', views.logout, name="logout"),
    path('reset-password', PasswordResetView.as_view(template_name = "forgot-passwrod.html"), name='password_reset'), 
    path('reset-password/done', PasswordResetDoneView.as_view(template_name = "password-success.html"), name='password_reset_done'), 
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(template_name = "change-password.html"), name='password_reset_confirm'), 
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name='password_reset_complete'),
    
    # path('forgot_password/', auth_views.PasswordResetView.as_view(template_name = "forgot-passwrod.html"), name ='reset_password'),
    # path('password_success/', auth_views.PasswordResetDoneView.as_view(template_name = "password-success.html"), name ='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "change-password.html"), name ='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete')
    # path('users/password_reset/', auth_views.PasswordResetView.as_view(
    #     template_name='users/password_reset.html',
    #     email_template_name='users/password_reset_email.html',
    #     subject_template_name='users/password_reset_subject.txt',
    #     success_url='/users/password_reset/done/'),
    #     name='password_reset'
    # ),
    # path('users/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='users/password_reset_done.html'),
    #     name='password_reset_done'
    # ),
    # path('users/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='users/password_reset_confirm.html',
    #     success_url='/users/reset/done/'),
    #     name='password_reset_confirm'
    # ),
    # path('users/reset/done/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='users/password_reset_complete.html'),
    #     name='password_reset_complete'
    # ),
]

    


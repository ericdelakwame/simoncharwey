from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,  
)
from django.urls import reverse, reverse_lazy
from .views import(
    RegisterUser, profile, UserChangeView, UpdateUserView
)


app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(
        template_name='accounts/forms/login_form.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('profile', profile, name='profile'),
    path('change/password', PasswordChangeView.as_view(template_name='accounts/registration/password_change_form.html',
         success_url=reverse_lazy('accounts:password_change_done'), extra_context={'header': 'Change Your Password'}), name='change_password'),
    path('password/change/done', PasswordChangeDoneView.as_view(
        template_name='accounts/registration/password_change_done.html'), name='password_change_done'),

    path('password/reset', PasswordResetView.as_view(template_name='accounts/registration/password_reset_form.html', email_template_name='accounts/registration/password_reset_email.html',
         subject_template_name='accounts/registration/password_reset_subject.txt', success_url=reverse_lazy('accounts:password_reset_done'), extra_context={'header': 'Reset Your Password'}, from_email='support@africandesignmatters.com'), name='password_reset'),

    path('password/reset/done', PasswordResetDoneView.as_view(
        template_name='accounts/registration/password_reset_done.html'), name='password_reset_done'),

    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/registration/password_reset_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),
    path('password/reset/complete', PasswordResetCompleteView.as_view(template_name='accounts/registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('change/account/<int:pk>', UserChangeView.as_view(), name='change_account'),
    
    path('update/user/<int:pk>', UpdateUserView.as_view(), name='update_user'),
]

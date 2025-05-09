from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'users'
urlpatterns = [
    # CORE
    path(route='home/',view=HomeView.as_view(),name='home'),
    path(route='register/',view=UserCreationView.as_view(),name='user_creation'),
    
    # AUTH
    path(route='log-in/',view=CustomLoginView.as_view(),name='login'),
    path(route='log-out/',view=CustomLogoutView.as_view(),name='logout'),

    # ADMIN
    path(route='admin-home/',view=AdminIndexView.as_view(),name='admin_home'),
    path(route='confirm-logout/',view=AdminLogoutConfirmView.as_view(),name='admin_confirm_logout'),
    path(route='user-settings/',view=AdminUserSettingsView.as_view(),name='user_settings'),
    path(route='user-profile/',view=AdminUserProfileView.as_view(),name='user_profile'),
    path(route='user-set-new-password/',view=AdminUserSetNewPasswordView.as_view(),name='user_set_new_password'),
    
    # PASSWORD RECOVERY
    path(route='password-recovery-request/',view=PasswordResetCustomView.as_view(),name='password_recovery_request'),
    path(route='password-recovery-request-done/',view=PasswordResetDoneCustomView.as_view(),name='password_recovery_request_done'),
    path(route='password-recovery-form/<uidb64>/<token>/',view=PasswordResetConfirmCustomView.as_view(),name='password_reset_form'),
    path(route='password-recovery-done/',view=PasswordResetCompleteCustomView.as_view(),name='password_reset_done'),
    
]

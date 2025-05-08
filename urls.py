from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    #CORE
    path(route='home/',view=HomeView.as_view(),name='home'),
    path(route='register/',view=UserCreationView.as_view(),name='user_creation'),
    
    #AUTH
    path(route='log-in/',view=CustomLoginView.as_view(),name='login'),
    path(route='log-out/',view=CustomLogoutView.as_view(),name='logout'),

    #ADMIN
    path(route='admin-home/',view=AdminIndexView.as_view(),name='admin_home'),
    path(route='confirm-logout/',view=AdminLogoutConfirmView.as_view(),name='admin_confirm_logout'),
    path(route='user-settings/',view=AdminUserSettingsView.as_view(),name='user_settings'),
    path(route='user-profile/',view=AdminUserProfileView.as_view(),name='user_profile'),
    path(route='user-set-new-password/',view=AdminUserSetNewPasswordView.as_view(),name='user_set_new_password')
]

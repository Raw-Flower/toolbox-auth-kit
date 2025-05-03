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
    path(route='admin-confirm-logout/',view=AdminLogoutConfirmView.as_view(),name='admin_confirm_logout'),
]

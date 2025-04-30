from django.urls import path
from .views import HomeView, UserCreationView, LoginView

app_name = 'users'
urlpatterns = [
    path(route='home',view=HomeView.as_view(),name='home'),
    path(route='register',view=UserCreationView.as_view(),name='user_creation'),
    path(route='log-in',view=LoginView.as_view(),name='login')
]

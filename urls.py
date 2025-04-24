from django.urls import path
from .views import HomeView, UserCreationView

app_name = 'users'
urlpatterns = [
    path(route='home',view=HomeView.as_view(),name='home'),
    path(route='user_creation',view=UserCreationView.as_view(),name='user_creation')
]

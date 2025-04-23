from django.urls import path
from .views import index

app_name = 'users'
urlpatterns = [
    path(route='index',view=index,name='index')
]

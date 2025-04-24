from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import UserCreationForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'users/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'home'
        return context
    
class UserCreationView(FormView):
    template_name = 'users/users_create.html'
    form_class = UserCreationForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'user_creation'
        return context
    

 
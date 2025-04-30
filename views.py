from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserCreationForm
from .utils import split_forms, saveModelsInfo

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
    success_url = reverse_lazy('users:home')
    
    def get_context_data(self, **kwargs):
        user_forms = split_forms(self.get_form())
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'user_creation'
        context['basic_form'] = user_forms.get('basic_form')
        context['profile_form'] = user_forms.get('profile_form')
        return context

    #Handle save function
    def form_valid(self, form):
        result = saveModelsInfo(form.cleaned_data)
        if result:
            messages.success(request=self.request, message='You have been successfully registered.')
            return super().form_valid(form)
        messages.error(request=self.request, message='A critical error was found while saving the user data, please contact with the system administrator.')
        return self.render_to_response(self.get_context_data(form=form))
    
    def form_invalid(self, form):
        messages.error(request=self.request, message='Your data contains some errors. Please check and try again.')
        return self.render_to_response(self.get_context_data(form=form))
        
    #Handle form validation 
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class LoginView(LoginView):
    template_name = 'users/login.html'

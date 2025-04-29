from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import UserCreationForm
from .utils import split_forms, cleanAttrs
from .models import UserProfile

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
        users_forms = split_forms(self.get_form())
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'user_creation'
        context['basic_form'] = users_forms[0]
        context['profile_form'] = users_forms[1]
        return context
        
    #Handle save function
    def form_valid(self, form):
        print(form.cleaned_data)
        user_fields = ['username','password','first_name','last_name']
        profile_fields = cleanAttrs([i.name for i in UserProfile._meta.get_fields()]) 
        print(profile_fields)
        return ''
        #return super().form_valid(form)
    
    #Handle form validation 
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

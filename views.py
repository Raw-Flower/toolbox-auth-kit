from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import UserCreationForm, CustomAuthForm, UserNewPasswordForm
from .utils import split_forms, saveModelsInfo, build_init_data, updateModelsInfo
from .mixins import NeverBrowserCache, SecureView

# Create your views here.
class HomeView(NeverBrowserCache, TemplateView):
    template_name = 'users/core/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'home'
        return context
    
class UserCreationView(FormView):
    template_name = 'users/core/users_create.html'
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
    
class CustomLoginView(NeverBrowserCache, LoginView):
    template_name='users/auth/login.html'
    form_class = CustomAuthForm
    success_url = reverse_lazy('users:admin_home')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            success_url = self.get_success_url()
            return HttpResponseRedirect(success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_invalid(self, form):
        messages.error(request=self.request, message="Your username and password didn't match. Please try again.")
        return super().form_invalid(form)

class CustomLogoutView(SecureView, LogoutView):
    template_name='users/auth/logout.html'
    success_url = reverse_lazy('users:home')
    
    def post(self, request, *args, **kwargs):
        messages.success(request=self.request, message="You have been logout successfully.")
        return super().post(request, *args, **kwargs)

class AdminIndexView(SecureView, TemplateView):
    template_name = 'users/admin/index.html'
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'admin_home'
        return context

class AdminLogoutConfirmView(SecureView, TemplateView):
    template_name = 'users/admin/confirm_logout.html'
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'confirm_logout'
        return context
    
class AdminUserSettingsView(SecureView, TemplateView):
    template_name = 'users/admin/user_settings.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'user_settings'
        return context
    
class AdminUserProfileView(SecureView, FormView):
    template_name = 'users/admin/user_profile.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('users:admin_home')
    
    def get_context_data(self, **kwargs):
        init_data = build_init_data(self.request.user)
        user_forms = split_forms(UserCreationForm(initial=init_data))
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'user_settings'
        context['profile_form'] = user_forms.get('profile_form')
        return context
    
    def form_valid(self, form):
        result = updateModelsInfo(self.request.user, form.cleaned_data)
        if result:
            messages.success(request=self.request, message='You have been updated your profile information successfully.')
            return super().form_valid(form)
        messages.error(request=self.request, message='A critical error was found while saving the user data, please contact with the system administrator.')
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        messages.error(request=self.request, message='Your data contains some errors. Please check and try again.')
        return self.render_to_response(self.get_context_data(form=form))
    
    #Handle form validation 
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        for field in list(form.fields):    
            if field in ['username','password','password_repeat']:
                del form.fields[field]        
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
    
class AdminUserNewPasswordView(SecureView, PasswordChangeView):
    template_name = 'users/admin/user_new_password.html'
    form_class = UserNewPasswordForm
    success_url = reverse_lazy('users:admin_home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'user_settings'
        return context
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator,EmailValidator,RegexValidator,ProhibitNullCharactersValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import re

def checkPasswordNumber(value):
    if not re.search(r'[0-9]',value):
        raise ValidationError(
            message=_("Password field should contain at least 1 number value."),
            code='missing_number'
        )
    return value

def checkPasswordUpper(value):
    if not re.search(r'[A-Z]',value):
        raise ValidationError(
            message= _("Password field should contain at least 1 uppercase value"),
            code='missing_upper'
        )
    return value

def checkPasswordSpecial(value):
    if not re.search(r'[!@#$%&*._-]',value):
        raise ValidationError(
            message=_("Password field should contain at least 1 special character.\nAllow characters are ! @ # $ % & * . _ -"),
            code='missing_special'
        )
    return value
        
class UserCreationForm(forms.Form):
    first_name = forms.CharField(
        label=_('First name'),        
        help_text=_('Simple...your name'),
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        ),
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(3),
            MaxLengthValidator(50),
            RegexValidator(
                regex='^[a-zA-Z ]+$',
                message=_('This field contains unvalid characters.'),
                code='invalid_characters'
            )
        ]
    )
    
    last_name = forms.CharField(
        label=_('Last name'),
        help_text=_('Another simple, your last name.'),
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        ),                    
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(3),
            MaxLengthValidator(25),
            RegexValidator(
                regex='^[a-zA-Z ]+$',
                message=_('This field contains unvalid characters.'),
                code='invalid_characters'
            )
        ]
    )
    
    email = forms.EmailField(
        label=_('Email'), 
        help_text=_('Please set a real email :)'),
        widget=forms.EmailInput(
            attrs={'class':'form-control'}
        ),
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(5),
            MaxLengthValidator(25),
            EmailValidator,
        ]
    )
    
    username = forms.CharField(
        label=_('Username'),
        help_text=_('A really creative username for our app.'),
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        ),
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(5),
            MaxLengthValidator(25),
            RegexValidator(
                regex='^[a-zA-Z0-9._-]+$',
                message=_('This field contains invalid characters. Allowed characters are letters, numbers, period, underscore, and hyphen.'),
                code='invalid_characters'
            )
        ]
    )
    
    password = forms.CharField(
        label=_('Password'),
        help_text=_('Secret key.'),
        widget=forms.PasswordInput(
            attrs={'class':'form-control'}
        ),
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(8),
            MaxLengthValidator(25),
            RegexValidator(
                regex='^[a-zA-Z0-9._!@#$%&*-]+$',
                message=_('This field contains invalid characters.\nAllowed characters are ! @ # $ % & * . _ - '),
                code='invalid_characters'
            ),
            checkPasswordNumber,
            checkPasswordUpper,
            checkPasswordSpecial
        ]
    )
    
    password_repeat = forms.CharField(
        label=_('Repeat password'),
        help_text=_('Secret key(again).'),
        widget=forms.PasswordInput(
            attrs={'class':'form-control'}
        ),
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(8),
            MaxLengthValidator(25),
            RegexValidator(
                regex='^[a-zA-Z0-9._!@#$%&*-]+$',
                message=_('This field contains invalid characters.\nAllowed characters are ! @ # $ % & * . _ - '),
                code='invalid_characters'
            ),
            checkPasswordNumber,
            checkPasswordUpper,
            checkPasswordSpecial
        ]
    )
    
    location = forms.CharField(
        label=_('Location'),
        help_text=_('Where are you right now?'),
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        ),                    
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(10),
            MaxLengthValidator(50),
            RegexValidator(
                regex='^[a-zA-Z, /]+$',
                message=_('This field contains unvalid characters.'),
                code='invalid_characters'
            )
        ]
    )
    
    contact_phone = forms.CharField(
        label=_('Contact phone'),
        help_text=_('999 999 999'),
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        ),                    
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(5),
            MaxLengthValidator(30),
            RegexValidator(
                regex='^[+0-9 -]+$',
                message=_('This field contains unvalid characters.'),
                code='invalid_characters'
            )
        ]
    )
    
    about_me = forms.CharField(
        label=_('Bio'),
        help_text=_('Insights about you.'),
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'rows':'3',
                'style':'max-width:500px;'
            }
        ),                    
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(5),
            MaxLengthValidator(100),
            RegexValidator(
                regex='^[a-zA-Z0-9 ]+$',
                message=_('This field contains unvalid characters.'),
                code='invalid_characters'
            )
        ]
    )
        
    address = forms.CharField(
        label=_('Address'),
        help_text=_('Current address about your home'),
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'rows':'3',
                'style':'max-width:500px;'
            }
        ),                    
        validators=[
            ProhibitNullCharactersValidator,
            MinLengthValidator(5),
            MaxLengthValidator(100),
            RegexValidator(
                regex='^[a-zA-Z0-9-# ]+$',
                message=_('This field contains unvalid characters.'),
                code='invalid_characters'
            )
        ]
    )
    
    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise ValidationError(
                message=_("Password fields must match."),
                code='password_match'
            )
        return password_repeat
    
    def clean_username(self):
        not_allow_username = ['root','admin','administrator','administrador','system','admon']
        username2check = self.cleaned_data.get('username')
        if (User.objects.filter(username=username2check).exists()):
            raise ValidationError(
                message=_("This username is already taken. please try with another one."),
                code='username_taken'
            )
        else:
            for word in not_allow_username:
                if username2check.find(word) != -1:
                    raise ValidationError(
                        message=_("The username field contains prohibited characters or words, please change it."),
                        code='invalid_words'
                    )
        return username2check
    
class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        ),
        validators=[
            ProhibitNullCharactersValidator,
            MaxLengthValidator(25),
            RegexValidator(
                regex='^[a-zA-Z0-9._-]+$',
                message=_('This field contains invalid characters. Allowed characters are letters, numbers, period, underscore, and hyphen.'),
                code='invalid_characters'
            )
        ]
    )
    
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={'class':'form-control'}
        ),
        validators=[
            ProhibitNullCharactersValidator,
            MaxLengthValidator(25),
            RegexValidator(
                regex='^[a-zA-Z0-9._!@#$%&*-]+$',
                message=_('This field contains invalid characters.\nAllowed characters are ! @ # $ % & * . _ - '),
                code='invalid_characters'
            )
        ]
    )
# 🧰 Toolbox Project - Users APP

![Toolbox Badge](https://img.shields.io/badge/Toolbox-Auth%20Kit-blue?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

> A professional Django application that centralizes essential tools for registered users. Focused on user experience, security, modularity, and strict adherence to Django principles such as DRY (Don't Repeat Yourself).

---

## 🚀 Main Features

### 🔐 Authentication & Security
- User registration with strict field validation  
- Secure session-based login system  
- Password recovery flow via email (reset request, confirmation, and success pages)  
- Redirection of authenticated users away from public pages like login/register  
- Protected views using `LoginRequiredMixin` + `never_cache` to prevent back navigation after logout  

### 👤 User Profile Management
- Single form that combines data from both `User` and `UserProfile` models  
- Visual form split into `basic_form` and `profile_form`  
- Custom `build_init_data()` for smart initialization  
- `split_forms()` used to organize rendering without duplicating logic  
- Custom validations and conditional required fields for clean UX  

### 🧭 Clean Navigation Experience
- Admin dashboard and personal profile view  
- Automatic redirect logic based on login/session state  
- Organized template structure for `base`, `auth`, `core`, `admin`, and `includes`  

### 🛠 Technical Best Practices
- Reusable mixins: `SecureView`, `RedirectAuthenticatedUserMixin`  
- Modular separation: logic in `utils.py`, `mixins.py`  
- DRY-compliant helpers: `build_init_data()`, `update_user_and_profile()`, `split_forms()`  
- Custom password reset form with inline validation: `PasswordResetCustomForm`  
- Full password reset cycle using Django's `PasswordResetView` and custom templates  

---

## 📁 Templates Structure

```
templates/users/
├── admin/
│   ├── confirm_logout.html
│   ├── index.html
│   ├── user_profile.html
│   ├── user_set_new_password.html
│   └── user_settings.html
├── auth/
│   ├── login.html
│   └── logout.html
├── base/
│   ├── admin_base.html
│   ├── main_base.html
│   └── standard_base.html
├── core/
│   ├── index.html
│   ├── password_recovery_done.html
│   ├── password_recovery_email.html
│   ├── password_recovery_form.html
│   ├── password_recovery_request.html
│   ├── password_recovery_request_done.html
│   └── users_create.html
└── includes/
    ├── bootstrap_css.html
    ├── bootstrap_js.html
    ├── form_render.html
    └── messages.html
```

## 🔧 Important Configuration Steps

Before testing the full functionality of the Users App, make sure to follow these **critical setup steps**:

---

### ⚙️ 1. Django Settings – Login Configuration

In your `settings.py`, define the following redirect routes for login, logout, and default user navigation:

```python
# LOGIN CONFIG
LOGIN_REDIRECT_URL = 'users:admin_home'
LOGIN_URL = 'users:login'
LOGOUT_REDIRECT_URL = 'users:home'
```

These ensure users are properly redirected during authentication workflows.

---

### 📩 2. Email Configuration – Console Output

To simulate password recovery and email-based flows in development, enable Django’s console email backend:

```python
# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

📬 All password reset and email notifications will now print directly to your terminal during development.

---

### 🧩 3. Custom Template Tag – Form Validation Class

You must add this **custom template tag** to enhance form field rendering with Bootstrap validation classes.

```python
from django import template

register = template.Library()

@register.filter(name='setValidationClass')
def setValidationClass(input):
    bootstrap_class = ''
    if (input.data != None) and (input.data != []):
        if input.errors:
            bootstrap_class = 'is-invalid'
        else:
            bootstrap_class = 'is-valid'
    return input.as_widget(attrs={'class': 'form-control ' + bootstrap_class})
```

📝 **Important**:  
By default configuration on Toolbox project the template tags file is call `custom_tags.py`, be sure to update all references to it, including:

- `templates/users/includes/form_render.html`

---

✅ With these steps configured, your application will:
- Provide correct login/logout redirects
- Dynamically apply form validation styling using Bootstrap

---

## 🤝 Credits

Thanks for following the development of Toolbox project on GitHub. Contributions and feedback are welcome to continue improving and scaling the platform.

---

> Built with Django ❤️

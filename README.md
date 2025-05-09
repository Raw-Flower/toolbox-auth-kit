# 🧰 Toolbox Project - Users APP

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

---

## 🤝 Credits

Thanks for following the development of Toolbox App on GitHub. Contributions and feedback are welcome to continue improving and scaling the platform.

---

> Built with Django ❤️

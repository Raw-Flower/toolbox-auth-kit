from django.contrib.auth.models import User
from .models import UserProfile

def split_forms(form):
    basic_form = [] 
    profile_form = []
    for field in form:
        if field.name in ['username','password','password_repeat']:
            basic_form.append(field)
        else: 
            profile_form.append(field)
    return {
        'basic_form':basic_form,
        'profile_form':profile_form,
    } 

def getUserFields():
    return [i.name for i in User._meta.get_fields()]

def getProfileFields():
    return [i.name for i in UserProfile._meta.get_fields()]

def getMappingValuesByModel(clean_data,model_fields):
    return {k:v for k,v in clean_data if k in model_fields}

def saveModelsInfo(cleaned_data):
    user_values = getMappingValuesByModel(cleaned_data.items(),getUserFields())
    profile_values = getMappingValuesByModel(cleaned_data.items(),getProfileFields())
    try:
        #save User record
        userInstance = User(**user_values)
        userInstance.set_password(user_values.get('password'))
        userInstance.is_staff = False #Not allow to login in admin panel
        userInstance.is_superuser = False #Not superuser permissions/rights
        userInstance.save()

        #save Profile record
        profileInstance = UserProfile(**profile_values)
        profileInstance.user = userInstance #Instance from user model
        profileInstance.save()
    except Exception as e:
        print(f'ERROR({type(e).__name__}): {e}')
        return False
    else:
        return True

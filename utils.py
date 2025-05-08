from django.contrib.auth.models import User
from .models import UserProfile
from django.forms.models import model_to_dict

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

def set_instance_values(instance,values2add):
    for key, value in values2add.items():
        setattr(instance,key,value)
    return instance

def build_init_data(user_instance):
    profile_instance = model_to_dict(UserProfile.objects.get(user=user_instance))# Instance to python dict
    profile_fields = getProfileFields()# Get all the fields names from UserProfile model
    initial_data = {field:profile_instance[field] for field in profile_fields if field not in ['status','createtime','updatetime','id','user']}# Build init data
    
    # Add User fields
    initial_data['first_name'] = user_instance.first_name
    initial_data['last_name'] = user_instance.last_name
    initial_data['email'] = user_instance.email
    
    # Return data
    return initial_data

def saveModelsInfo(cleaned_data):
    user_values = getMappingValuesByModel(cleaned_data.items(),getUserFields())
    profile_values = getMappingValuesByModel(cleaned_data.items(),getProfileFields())
    try:
        # Save User record
        userInstance = User(**user_values)
        userInstance.set_password(user_values.get('password'))
        userInstance.is_staff = False # Not allow to login in admin panel
        userInstance.is_superuser = False # Not superuser permissions/rights
        userInstance.save()

        # Save Profile record
        profileInstance = UserProfile(**profile_values)
        profileInstance.user = userInstance # Instance from user model
        profileInstance.save()
    except Exception as e:
        print(f'ERROR({type(e).__name__}): {e}')
        return False
    else:
        return True

def updateModelsInfo(user_instance,cleaned_data):
    user_values = getMappingValuesByModel(cleaned_data.items(),getUserFields())
    profile_values = getMappingValuesByModel(cleaned_data.items(),getProfileFields())
    
    try:
        # Set new values to instances
        user_instance = set_instance_values(user_instance,user_values)
        profile_instance = set_instance_values(UserProfile.objects.get(user=user_instance),profile_values)
        
        # Save updated information
        user_instance.save()
        profile_instance.save()
    except Exception as e:
        print(f'ERROR({type(e).__name__}): {e}')
        return False
    else:
        return True
    
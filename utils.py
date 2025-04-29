def split_forms(form):
    basic_form = [] 
    profile_form = []
    for field in form:
        if field.name in ['username','password','password_repeat']:
            basic_form.append(field)
        else: 
            profile_form.append(field)
    return (basic_form,profile_form)

def cleanAttrs(list2clean):
    attr2clean = ['id','user','createtime','updatetime']
    for item in list2clean:
        if item in attr2clean:
            list2clean.remove(item)
    return list2clean
            
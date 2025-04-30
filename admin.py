from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','status','createtime','updatetime']
    readonly_fields = ['user','createtime','updatetime']
    list_filter = ['status']
    ordering = ['id','-createtime']
    search_fields = ['user']
    
admin.site.register(UserProfile, UserProfileAdmin)

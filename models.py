from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StatusOptions(models.IntegerChoices):
    enable = (1,'Enable')
    disabled = (0,'Disabled')
    __empty__ = ('-- Status --')
    
class UserProfile(models.Model):
    user = models.OneToOneField(verbose_name='User', to=User, on_delete=models.CASCADE)
    location = models.CharField(verbose_name='Location', max_length=100)
    contact_phone = models.CharField(verbose_name='Contact phone', max_length=100)
    address = models.TextField(verbose_name='Address', max_length=100)
    about_me = models.TextField(verbose_name='Bio', max_length=100)
    status = models.IntegerField(verbose_name='Status', choices=StatusOptions.choices)
    createtime = models.DateTimeField(verbose_name='Createtime', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='Updatetime', auto_now=True)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profile"
        ordering = ['user']

    def __str__(self):
        return str(self.id)


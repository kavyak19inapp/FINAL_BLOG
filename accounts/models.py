from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
<<<<<<< HEAD
    user=models.ForeignKey(User,on_delete=models.CASCADE)
=======
    user=models.OneToOneField(User)
>>>>>>> 6c0dd6c914f92e653ee8e24941335be8686c999b
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    website=models.URLField(default='')
    phone=models.IntegerField(default=0)
<<<<<<< HEAD
=======

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)
>>>>>>> 6c0dd6c914f92e653ee8e24941335be8686c999b

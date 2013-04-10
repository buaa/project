from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.http import HttpResponse
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length = 30, blank=False, )
    self_potrait = models.ImageField(upload_to = 'photos',null=True,blank=True)
    #monitortask_count = models.IntegerField(default=0,help_text='do not edit this field, keep it lower than 20')

    def __unicode__(self):
        return self.user.username


class MonitorTask(models.Model):
    user = models.ForeignKey(User)
    monitor_type = models.BooleanField(default=1,help_text='ticked means monitor word')
    bloger_id = models.CharField(max_length=50,blank = True)
    bloger_name = models.CharField(max_length=50, blank = True)
    monitor_word = models.CharField(max_length=50, blank = True)
    trigger_type = models.CharField(max_length=50, blank = True)

    def __unicode__(self):
        return self.user.username


class MonitorAlarm(models.Model):
    TRIGGER_TYPE = (
    ('C', 'Contentalarm'),
    ('D', 'Levelalarm'),
    ('A', 'Both'),
)
    SENDING_TYPE = (
    ('E', 'Emailalarm'),
    ('P', 'Phonealarm'),
)
    monitor_task = models.OneToOneField(MonitorTask)
    trigger_type = models.CharField(max_length = 1,choices = TRIGGER_TYPE)
    sending_type = models.CharField(max_length = 1,choices = SENDING_TYPE)
    alarm_address = models.CharField(max_length = 30)
    alarm_text = models.CharField(max_length = 100)




#change the monitortask_count when monitor task created or delete
'''
def create_monitor_task_profile(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        userProfile = UserProfile.objects.get(user = user)
        userProfile.monitortask_count += 1
        userProfile.save()

post_save.connect(create_monitor_task_profile, sender=MonitorTask)


def delete_monitor_task_profile(sender, instance, **kwargs):
    user = instance.user
    userProfile = UserProfile.objects.get(user = user)
    userProfile.monitortask_count -= 1
    userProfile.save()

post_delete.connect(delete_monitor_task_profile, sender=MonitorTask)

#create a userprofile when a User created
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender= User)
'''

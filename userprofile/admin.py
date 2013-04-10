from django import forms
from django.forms.widgets import TextInput
from userprofile.models import *
from django.contrib import admin
from django.contrib.auth.admin import *

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    #inlines = (MonitorTaskInline, )

class MonitorTaskAdmin(admin.ModelAdmin):
    list_display = ('user','id', 'monitor_type', 'bloger_name','monitor_word')



class MonitorAlarmAdmin(admin.ModelAdmin):
    pass

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(MonitorTask, MonitorTaskAdmin)
admin.site.register(MonitorAlarm, MonitorAlarmAdmin)



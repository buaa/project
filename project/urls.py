from django.conf.urls import patterns, include, url
from userprofile.views import *
from login.views import *
#from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',index_form),
    url(r'^index/$',index_retrieve),
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),
    url(r'^accounts/loginform/$',  login_form),
    url(r'^accounts/loginform/login/$',  my_login),
    #url(r'^accounts/logout/$', logout),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)
#for showing image

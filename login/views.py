# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import *
from django.shortcuts import render_to_response
from userprofile.models import *


#redirect user to login page
def login_form(request):
     next = request.GET['next']
     return render_to_response('registration/login.html', {'next': next})

#the destination of form's submition
def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            next = request.POST['next']
            #Redirect to a success page.
            print next
            return HttpResponseRedirect(next)
        else:
            # Return a 'disabled account' error message
            return HttpResponse("invalid user")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("invalid user")
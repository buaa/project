# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index_form(request):
	return HttpResponseRedirect('/index/')
@login_required
def index_retrieve(request):
	return HttpResponse("This is index page")


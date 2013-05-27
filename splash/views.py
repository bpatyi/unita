import django.http as http

from django.template.response import TemplateResponse, HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render_to_response, redirect

from django.contrib.auth.decorators import login_required

from splash.models import *

def splash(request):

	splash = Splash.objects.all()[0]
  
	ctx = {
		'splash':splash,
	}
	
	return TemplateResponse(request, 'splash.html', ctx)
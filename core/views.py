import django.http as http

from django.template.response import TemplateResponse, HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.contrib.flatpages.models import FlatPage

from django.contrib.auth.decorators import login_required

from core.forms import *

def contact(request):
	from django.contrib import messages
	
	if request.method == "POST":
		contact_form = ContactForm(request.POST)
		
		if contact_form.is_valid():
			name = contact_form.cleaned_data['name']
			email = contact_form.cleaned_data['email']
			message = contact_form.cleaned_data['message']
			m=Message(name=name,email=email,message=message)
			m.save()
			messages.success(request, 'Thank you!!!')
			
	else:
		contact_form = ContactForm()
		
	ctx = {
		'contact_form':contact_form,
		}
		
	return TemplateResponse(request, 'contact.html',ctx)

def patrons(request):
	flatpage = get_object_or_404(FlatPage, url='/patrons/')

	if request.method == "POST":
		patron_form = PatronForm(request.POST)

		if patron_form.is_valid():
			first_name = patron_form.cleaned_data['first_name']
			last_name = patron_form.cleaned_data['last_name']
			payer_business_name = patron_form.cleaned_data['payer_business_name']
			payer_email = patron_form.cleaned_data['payer_email']
			contact_phone = patron_form.cleaned_data['contact_phone']
			address_zip = patron_form.cleaned_data['address_zip']
			address_city = patron_form.cleaned_data['address_city']
			address_country = patron_form.cleaned_data['address_country']
			address_street = patron_form.cleaned_data['address_street']

			patron = Patron(first_name=first_name, last_name=last_name, payer_business_name=payer_business_name, payer_email=payer_email, contact_phone=contact_phone,
				address_zip=address_zip, address_city=address_city, address_country=address_country, address_street=address_street )
			patron.save()
	else:
		patron_form = PatronForm()
		
	ctx = {
		'patron_form':patron_form,
		'flatpage': flatpage,
		}
		
	return TemplateResponse( request, 'patrons.html',ctx )
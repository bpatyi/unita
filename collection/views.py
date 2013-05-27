import django.http as http

from django.template.response import TemplateResponse, HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render_to_response, redirect

from django.contrib.auth.decorators import login_required

from collection.models import *

def collection(request):
	if request.user.is_authenticated():
		try:
			collections = Collection.objects.all()
		except Collection.DoesNotExist:
			raise Http404
	else:
		try:
			collections = Collection.objects.filter(is_private=False)
		except Collection.DoesNotExist:
			raise Http404


	all = {}

	if collections:
		for collection in collections:
			images = Image.objects.filter(collection=collection)
			all[collection] = images.order_by('?')[:1]

	ctx = {
		'collections': all,
	}

	return TemplateResponse(request, 'collection.html', ctx)

def album(request, slug = None):
	try:
		album = Collection.objects.get(slug = slug)
	except Collection.DoesNotExist:
		raise Http404

	if album:
		images = Image.objects.filter(collection=album)
	
	ctx = {
		'album': album,
		'images': images,
	}

	return TemplateResponse(request, 'album.html', ctx)

def image(request, slug = None, img_slug = None):
	try:
		image = Image.objects.get(collection__slug=slug, slug=img_slug)
	except Image.DoesNotExist:
		raise Http404

	photos = Image.objects.filter(collection__slug=slug)

	for k,v in enumerate(photos):
		if v.slug == image.slug:
			break

	photos = list(photos)

	if k == len(photos)-1:
		next = photos[0]
	else:
		next = photos[k+1]

	ctx = {
		'image':image,
		'prev':photos[k-1],
		'next':next,
		'photos':photos,
		
	}

	return TemplateResponse(request, 'image.html', ctx)
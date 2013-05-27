from django.conf.urls import patterns, include, url
from django.conf import settings
from filebrowser.sites import site
from django.contrib.auth.views import logout, login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^login/$', login , {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/about/' }, name='logout'),

    url(r'^$', 'splash.views.splash', name='splash'),
    url(r'^collection/$', 'collection.views.collection', name='collection'),
    url(r'^collection/(?P<slug>[-\w]+)/$', 'collection.views.album', name='album'),
    url(r'^collection/(?P<slug>[-\w]+)/(?P<img_slug>[-\w]+)/$', 'collection.views.image', name='image'),

    url(r'^contact/$', 'core.views.contact', name="contact"),

    url(r'^patrons/$', 'core.views.patrons', name="patrons"),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'), "django.views.static.serve", {"document_root": settings.STATIC_ROOT}),
    )
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    )
from django.contrib  import admin
from collection.models import *
from django.conf import settings

class CollectionAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',)

class ImageAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',)

admin.site.register(Artist)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Image, ImageAdmin)
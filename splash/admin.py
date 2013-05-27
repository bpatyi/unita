from django.contrib  import admin
from splash.models import Splash
from django.conf import settings

class SplashAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',)
 
admin.site.register(Splash, SplashAdmin)

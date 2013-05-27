from django.contrib  import admin
from core.models import * 

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

class FlatpageForm(FlatpageFormOld):
    class Meta:
        model = FlatPage
 
class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

class MessageAdmin(admin.ModelAdmin):
	list_display = ('read', 'name', 'email','message','date')
	class Media:
		js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/grappelli/tinymce_setup/tinymce_setup.js',)

admin.site.register(Message,MessageAdmin)

admin.site.register(MenuItem)

admin.site.register(Patron)




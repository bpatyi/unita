from django.contrib  import admin
from django import forms
from core.models import *

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

class SubMenuForm(forms.ModelForm):

    class Meta:
        model = SubMenu

    def clean(self):
        cleaned_data = super(SubMenuForm, self).clean()

        url = cleaned_data.get('url')
        flatpage = cleaned_data.get('flatpage')

        if url and flatpage:
            raise forms.ValidationError("Please, just fill in one field only. Flatpage or Url.")

        if not(url or flatpage):
            raise forms.ValidationError("Please, fill in flatpage or url field.")

        return cleaned_data

class SubMenuInline(admin.TabularInline):
    model = SubMenu

class SubMenuAdmin(admin.ModelAdmin):
    form = SubMenuForm

class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem

    def clean(self):
        cleaned_data = super(MenuItemForm, self).clean()

        url = cleaned_data.get('url')
        flatpage = cleaned_data.get('flatpage')
        only = cleaned_data.get('only_mainmenu')

        if only==False:
            if url and flatpage:
                raise forms.ValidationError("Please, just fill in one field only. Flatpage or Url.")

            if not(url or flatpage):
                raise forms.ValidationError("Please, fill in flatpage or url field.")

        return cleaned_data

class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm

    inlines = [
        SubMenuInline,
    ]

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

admin.site.register(MenuItem, MenuItemAdmin)

admin.site.register(SubMenu, SubMenuAdmin)

admin.site.register(Patron)




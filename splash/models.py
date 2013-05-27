from django.db import models
from django import forms
from filebrowser.fields import FileBrowseField

class Splash(models.Model):
    text = models.TextField()
    image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True, null=True)
	
    def __unicode__(self):
        return u"%s - %s" % (self.text,self.image)

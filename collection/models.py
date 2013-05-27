from django.db import models
from autoslug import AutoSlugField
from easy_thumbnails.fields import ThumbnailerImageField

class Artist(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return u"%s" % (self.name)

class Collection(models.Model):
	order = models.IntegerField()
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from='name')
	description = models.TextField()
	created = models.DateField(auto_now_add=True)
	artist = models.ForeignKey(Artist)
	is_private = models.BooleanField(default=False, verbose_name=u'private')

	class Meta:
		ordering = ('order',)

	def __unicode__(self):
		return u"%d - %s - %s" % (self.order, self.artist, self.name)

class Image(models.Model):
	order = models.IntegerField()
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from='name')
	description = models.TextField()
	created = models.DateField(auto_now_add=True)
	collection = models.ForeignKey(Collection)
	photo = ThumbnailerImageField(upload_to='photos', blank=True)

	class Meta:
		ordering = ('order',)

	def __unicode__(self):
		return u"%d - %s - %s" % (self.order, self.collection.name, self.name)
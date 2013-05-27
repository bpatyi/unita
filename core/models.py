from django.db import models
from django_countries import CountryField

class MenuItem(models.Model):
	order = models.IntegerField()
	title = models.CharField(max_length=50)
	url = models.CharField(('URL'),max_length=100,db_index=True)
	
	class Meta:
		ordering=('order',)
		
	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)
		
	def get_absolute_url(self):
		return self.url

class Message(models.Model):
	read = models.BooleanField(default=False)
	name = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateField(auto_now=True)
	
	class Meta:
		ordering = ('-date',)
		
	def __unicode__(self):
		return u"%s" % (self.message[0:min(len(self.message),25)])

class Patron(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30,)
	payer_business_name = models.CharField(max_length=50, verbose_name=u'Business Name')
	payer_email = models.EmailField(verbose_name=u'Email address')
	contact_phone = models.IntegerField()
	payment_date = models.DateField(auto_now_add = True)
	#address = AddressField()
	address_zip = models.IntegerField()
	address_city = models.CharField(max_length=40,)
	address_country = CountryField()
	address_street = models.CharField(max_length=50)

	class Meta:
		ordering=('payment_date',)

	def __unicode__(self):
		return u"%s %s" % (self.first_name, self.last_name)
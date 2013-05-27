from django.db import models
from django_countries import CountryField
from django.contrib.flatpages.models import FlatPage

class MenuItem(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=50)
    url = models.CharField('URL',max_length=100,db_index=True, blank=True, default='')
    flatpage = models.ForeignKey(FlatPage, blank=True, default='', null=True)
    only_mainmenu = models.BooleanField(verbose_name='Only Main Menu', default=False, blank=True, help_text="Check, if this menu have submenus.")

    class Meta:
        ordering=('order',)

    def __unicode__(self):
        return u"%s -- %s" % (self.title, self.url)

    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.flatpage:
            return self.flatpage.url


class SubMenu(models.Model):
    menu = models.ForeignKey(MenuItem)
    title = models.CharField(max_length=50)
    url = models.CharField('URL',max_length=100,db_index=True, blank=True, default='')
    flatpage = models.ForeignKey(FlatPage, blank=True, default='', null=True)

    def __unicode__(self):
        return u"%s -- %s" % (self.title, self.url)

    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.flatpage:
            return self.flatpage.url


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

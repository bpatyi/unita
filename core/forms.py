from django import forms  
from core.models import *

class ContactForm(forms.ModelForm):
	class Meta:
		model = Message
		exclude = ('read',)

class PatronForm(forms.ModelForm):
	class Meta:
		model = Patron
		exclude = ('-payment_date',)

	def __init__(self, *args, **kwargs):
		super(PatronForm, self).__init__(*args, **kwargs)
		self.fields['payer_business_name'].required = False

	def clean(self):
		first_name = self.cleaned_data.get('first_name')
		if first_name is None:
			raise forms.ValidationError('Please enter your first name!')

		last_name = self.cleaned_data.get('last_name')
		if last_name is None:
			raise forms.ValidationError('Please enter your last name!')

		payer_email = self.cleaned_data.get('payer_email')
		if payer_email is None:
			raise forms.ValidationError('Please enter your email address!')

		contact_phone = self.cleaned_data.get('contact_phone')
		if contact_phone is None:
			raise forms.ValidationError('Please enter your phone number!')

		address_zip = self.cleaned_data.get('address_zip')
		if address_zip is None:
			raise forms.ValidationError('Please enter your address zip!')

		address_city = self.cleaned_data.get('address_city')
		if address_city is None:
			raise forms.ValidationError('Please enter your city name!')

		address_country = self.cleaned_data.get('address_country')
		if address_country is None:
			raise forms.ValidationError('Please enter your country name!')

		address_street = self.cleaned_data.get('address_street')
		if address_street is None:
			raise forms.ValidationError('Please enter your address street!')

		return self.cleaned_data
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import int_to_base36
from django.template import Context, loader
from django import forms
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import AuthenticationForm
from clients.models import Ticket

class TicketForm(forms.ModelForm):
	'''
	def save(self, user=request.user):
		print user.username
		print 'saving form in form.py'
		ticket = super(TicketForm, self).save(commit=False)
		ticket.ticket = self.cleaned_data['ticket']
		ticket.urgent = self.cleaned_data['urgent']
		ticket.website= self.cleaned_data['website']
		'''
	class Meta:
		model = Ticket
		fields = ['title', 'ticket','urgent', 'client', 'website']

from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from accounts.forms import UserCreationForm #UserProfileForm
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings
from django.utils.http import urlquote, base36_to_int
from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite
from clients.forms import TicketForm

# Create your views here.
def ticket(request):
	html = 'page for submitting tickets'
	user = request.user
	print user.username
	if request.method=='POST':
		form = TicketForm(request.POST)
		print 'form method == post'
		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.user = request.user
			print ticket.user
			ticket.save()
			print 'saved form'
			return HttpResponseRedirect('/ticket')
		else: print 'form not valid'
	else:
		form = TicketForm(request.POST)
	print 'request.method =! post'
	return render(request, 'ticket.html',{'html':html,'user':user,'form':form})
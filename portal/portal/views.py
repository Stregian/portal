# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from portal.forms import RegistrationForm, TicketForm

def index(request):
    html = 'Hello world'
    return HttpResponse(html)
'''
def login(request):
    html = 'login page for clients - under construction'
    return HttpResponse(html)
'''
def account_profile(request):
    
    return HttpResponse(stuff)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/register/success')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

def register_success(request):
    return render(request, 'registration/register_success.html')

def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            new_ticket = form.save()
            return HttpResponse('/ticket/sent')

    else:
        form = TicketForm()
    return render(request, 'ticket.html')
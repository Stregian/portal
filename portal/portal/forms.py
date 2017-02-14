from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from clients import models
'''
class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label = "Username", required=True)
    email1 = forms.EmailField(label="Email address", required=True)
    email2 =forms.EmailField(label="Repeat email address", required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput())
    
    def clean(self):    
        cleaned_data = super(RegistrationForm, self).clean()
        email1 = self.cleaned_data.get('email1')
        email2 = self.cleaned_data.get('email2')
        if email1 and email2 and email1 != email2:
            raise forms.ValidationError(_('Email addresses do not match'), code='email_mismatch')
        password1 = self.cleaneddata.get('password1')
        password2 = self.cleaneddata.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Passwords do not match'), code='password_mismatch')
        return self.cleaned_data


    class Meta:
        model = User
        fields = ("username", "email1", 'email2', "password1", "password2")

'''
class TicketForm(forms.ModelForm):
    ticket = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
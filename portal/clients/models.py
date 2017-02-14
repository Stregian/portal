from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
	title = models.CharField(max_length=254)
	email = models.EmailField(max_length=254)
	contact = models.CharField(max_length=20, verbose_name='Contact number')



	def __unicode__(self):
		return self.title

	def admin_url(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

class Website(models.Model):
	client = models.ForeignKey('Client')
	title = models.CharField(max_length=254)
	url = models.URLField()
	dob = models.DateField(verbose_name="Date of birth")

	def __unicode__(self):
		return self.title

	def admin_url(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

class Hosting(models.Model):
	website = models.ForeignKey('Website')
	client = models.ForeignKey('Client')
	cost = models.DecimalField(max_digits=7, decimal_places=2)
	renewal_date = models.DateField()	

	def renewal_date_order(self):
		return []

	renewal_date_order.admin_order_field = 'client'
	def __unicode__(self):
		return self.client.title

	class Meta: 
		verbose_name_plural ="Hosting"

	
	def renewal_date_passed(self):
		if datetime.datetime.now().day > self.renewal_date.day:
			return "Renewal date passed"
		else:
			return ""

	def admin_url(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))


class Employee(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	client = models.ForeignKey('Client', blank=True)

	def admin_url(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))


class Ticket(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	client = models.ForeignKey('Client')
	website = models.ForeignKey('Website')
	title = models.CharField(max_length=255, null = True)
	ticket = models.TextField()
	urgent = models.BooleanField(default=False)
	dob = models.DateTimeField(default=timezone.now())

	def __unicode__(self):
		return self.title


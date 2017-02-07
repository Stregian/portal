from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
import datetime
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType


# Create your models here.

class Client(models.Model):
	title = models.CharField(max_length=254)
	email = models.EmailField(max_length=254)
	contact = models.CharField(max_length=20)


	def __unicode__(self):
		return self.title


class Website(models.Model):
	fk = models.ForeignKey('Client', verbose_name='Client')
	title = models.CharField(max_length=254)
	url = models.URLField()
	dob = models.DateField()

	def __unicode__(self):
		return self.title
	def admin_url(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

class Hosting(models.Model):
	fk = models.ForeignKey('Website', verbose_name="Website")
	fk_client = models.ForeignKey('Client', verbose_name='Associated Client')
	cost = models.DecimalField(max_digits=7, decimal_places=2)
	renewal_date = models.DateField()	

	def renewal_date_order(self):
		return []

	renewal_date_order.admin_order_field = 'fk_client'
	def __unicode__(self):
		return self.fk.title

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
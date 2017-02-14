from django.contrib import admin
from models import Client, Website, Hosting, Employee, Ticket
import datetime
from django.utils.translation import ugettext_lazy as _
#from django.contrib.sites.models import Site
from django.core import urlresolvers
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

# Register your models here.
class HostingInline(admin.TabularInline):
    extra = 0
    model = Hosting
    pass
class WebsiteAdmin(admin.ModelAdmin):
    inlines = [HostingInline]
    search_fields = ['title']
    list_display = ('site','client','dob')
    
    def site(self,obj):
        return '<a href="%s">%s</a>' % (obj.admin_url(), obj.title)
    site.allow_tags = True

class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 0
    readonly_fields = ('title','url','dob')
    show_change_link = True
    pass

class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('title','email','contact')
    search_fields = ['title','email']
    inlines = [WebsiteInline]

class RenewalDatePassedListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Renewal_date_passed')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'soon-ness'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('passed', _('Passed due date')),
            ('today', _('Due today')),
            ('week', _('Due this week')),
            ('month', _('Due this month')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.

        if self.value() == 'passed':
            return queryset.filter(renewal_date__lt=datetime.datetime.now())
        if self.value() == 'today':
            return queryset.filter(renewal_date__gte=datetime.datetime.now(),
                                    renewal_date__lte=datetime.datetime.now() + datetime.timedelta(days=1))
        if self.value() == 'week':
            return queryset.filter(renewal_date__gte=datetime.datetime.now() + datetime.timedelta(days=1),
                                    renewal_date__lte=datetime.datetime.now() + datetime.timedelta(days=7))
        if self.value() == 'month':
            return queryset.filter(renewal_date__gte=datetime.datetime.now() + datetime.timedelta(days=7),
                                    renewal_date__lte=datetime.datetime.now() + datetime.timedelta(days=31))


class HostingAdmin(admin.ModelAdmin):
    model = Hosting
    ordering = ('renewal_date',)
    list_display = ( 'client', 'cost', 'renewal_date', 'renewal_date_passed','admin_site_url', 'website_url',)
    search_fields = ['website__title','client__title']
    list_filter = (RenewalDatePassedListFilter, )

    def client(self,obj):
        return '<a href="%s">%s</a>' % (obj.client.admin_url(), obj.client.title)
    client.allow_tags = True
    def website_url(self, obj):
        return '<a href="%s">%s</a>' % (obj.client.url, obj.client.title)
    website_url.allow_tags = True

    def admin_site_url(self,obj):
        return '<a href="%s">%s</a>' % (obj.client.admin_url(), obj.client.title)
    admin_site_url.allow_tags = True


class EmployeeInline(admin.StackedInline):
    model = Employee
    verbose_name_plural = 'employee'


class UserAdmin(admin.ModelAdmin):
    inlines = (EmployeeInline, )
    list_display = ('username', 'email')
    def client(self,obj):
        return '<a href="%s">%s</a>' % (obj.client.admin_url(), obj.client.title)
    client.allow_tags = True



admin.site.unregister(Site)
admin.site.register(Ticket)
admin.site.register(Client, ClientAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Hosting, HostingAdmin)
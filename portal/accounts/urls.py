from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',
    # Accounts
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name':'accounts/login.html' }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'template_name': 'accounts/logout.html'},name='logout'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', { 'template_name':'accounts/password_reset_done.html' }, name='password_reset_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'accounts/password_reset_form.html','email_template_name': 'accounts/password_reset_email.html'},name='password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$','django.contrib.auth.views.password_reset_confirm', {'template_name': 'accounts/password_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^signup/$','accounts.views.signup', {'template_name': 'accounts/signup_form.html','email_template_name': 'accounts/signup_email.html'}, name='signup_form'),   
    url(r'^signup/done/$', 'accounts.views.signup_done',  {'template_name': 'accounts/signup_done.html'}, name = 'signup_done'),
    url(r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'accounts.views.signup_confirm', name = 'signup_confirm'),
    url(r'^signup/complete/$', 'accounts.views.signup_complete', {'template_name': 'accounts/signup_complete.html'}, name = 'signup_complete'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',  {'template_name': 'accounts/password_change_form.html'},name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'accounts/password_change_done.html'},name='password_change_done'),   

    url(r'^accounts/profile/', 'accounts.views.profile', name = 'profile'),
    #url(r'^accounts/profile/details', 'accounts.views.profile_change', name ='profile_change'),
    url(r'^ticket', 'clients.views.ticket', name = 'ticket')
)
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



from django.views.decorators.csrf import csrf_protect

def login(request, *args, **kwargs):
    print "logging in"
    if request.method == 'POST':
        print 'hello world '
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    print form.username.value
    return views.login(request, *args, **kwargs)

@csrf_protect
def signup(request, template_name='accounts/signup.html', 
           email_template_name='accounts/signup_email.html',
           signup_form=UserCreationForm,
           token_generator=default_token_generator,
           post_signup_redirect=None):
    print "got to signup view"
    if post_signup_redirect is None:
        print 'post_signup redirect = None '
        post_signup_redirect = reverse('accounts.views.signup_done')
        print 'post signup redirect = ' + str(post_signup_redirect)
    if request.method == "POST":
        print "method was POST"
        form = signup_form(request.POST)
        if form.is_valid():
            print "form valid"
            opts = {}
            opts['use_https'] = request.is_secure()
            opts['token_generator'] = token_generator
            opts['email_template_name'] = None
            if not Site._meta.installed:
                opts['domain_override'] = RequestSite(request).domain  
            form.save(**opts)
            print "user saved"
            return HttpResponseRedirect(post_signup_redirect)
        else:
            print "form not valid"
    else:
        print "request not POST"
        form = signup_form()
    return render_to_response(template_name, {'form': form, 'form_page':'signup','page':'signup',},

                                   context_instance=RequestContext(request))

def signup_done(request, template_name='accounts/signup_done.html'):
    print "signup done called by reverse returning: "
    print str(render_to_response(template_name, 
                              context_instance=RequestContext(request)))
    return render_to_response(template_name, 
                              context_instance=RequestContext(request))

def signup_confirm(request, uidb36=None, token=None,
                   token_generator=default_token_generator,
                   post_signup_redirect=None):
    assert uidb36 is not None and token is not None #checked par url
    print(uidb36) 
    print(token)
    if post_signup_redirect is None:
        post_signup_redirect = reverse('accounts.views.signup_complete')
    try:
        uid_int = base36_to_int(uidb36)
    except ValueError:
        raise Http404

    user = get_object_or_404(User, id=uid_int)
    context_instance = RequestContext(request)

    if token_generator.check_token(user, token):
        context_instance['validlink'] = True
        user.is_active = True
        user.save()
    else:
        context_instance['validlink'] = False
    return HttpResponseRedirect(post_signup_redirect)

def signup_complete(request, template_name='account/signup_complete.html'):
    return render_to_response(template_name, 
                              context_instance=RequestContext(request, 
                                                              {'login_url': settings.LOGIN_URL}))

def profile(request):
    user = get_object_or_404(User, id=request.user.id)    
    print user.username + user.username
    #if request.method == POST:
    #    form = ProfileForm(request.POST)
    context = {'user':user}
    return render(request, 'accounts/profile.html', context)

def profile_change(request):

    if request.user.is_active:
        form = profile_form(request.POST)
        if request.method == POST:
            if form.is_valid():
                form.save()
            else:
                print 'form not valid'
    else:
        return 'please log in'
    return render_to_response('accounts/profile_change.html', {'form':form})
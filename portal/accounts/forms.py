from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import int_to_base36
from django.template import Context, loader
from django import forms
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(forms.ModelForm):
    username = forms.RegexField(label="Username", max_length=30, regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                                error_messages = {'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput,
                                help_text = "Enter the same password as above, for verification.")
    email1 = forms.EmailField(label="Email", max_length=75)
    email2 = forms.EmailField(label="Email confirmation", max_length=75,
                              help_text = "Enter your email address again. A confirmation email will be sent to this address.")
    

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2
    
    def clean_email1(self):
        email1 = self.cleaned_data["email1"]
        users_found = User.objects.filter(email__iexact=email1)
        if len(users_found) >= 1:
            raise forms.ValidationError("A user with that email already exist.")
        return email1

    def clean_email2(self):
        email1 = self.cleaned_data.get("email1", "")
        email2 = self.cleaned_data["email2"]
        if email1 != email2:
            raise forms.ValidationError("The two email fields didn't match.")
        return email2

    def save(self, commit=True, domain_override=None,
             email_template_name='registration/signup_email.html',
             use_https=False, token_generator=default_token_generator):
        print "saving form"
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email1"]
        user.is_active = False
        if commit:
            user.save()
            print 'commit true, saving user'
        if not domain_override:
            current_site = Site.objects.get_current()
            print current_site.name
            site_name = current_site.domain
            print site_name
            domain = current_site.domain
            print str(domain) 
        else:
            site_name = domain = domain_override
            print str(site_name) + 'domain_overidden'
        
        plain_text = loader.get_template('accounts/signup_email_plain.html')
        html = loader.get_template('accounts/signup_email.html')
        c = Context({
            'email': user.email,
            'domain': domain,
            'site_name': site_name,
            'uid': int_to_base36(user.id),
            'user': user,
            'token': token_generator.make_token(user),
            'protocol': use_https and 'https' or 'http',
            })
        print str(c['token']) +'user ID b_36 '+ str(c['uid'])
        html_content = html.render(c)
        text_content = plain_text.render(c)
        print 'signup email = ' +str(text_content)
        subject, from_email, to = "Confirmation link sent on %s" % site_name, 'the_team@crapidea.com', [user.email]
        email = EmailMultiAlternatives(subject, text_content, from_email, to)
        email.attach_alternative(html_content, "text/html")
        email.send()
        print str(user) + 'confirmation email sent'
        return user #why return this?


'''class UserProfileForm(forms.ModelForm):
    client = forms.CharField(max_length=50, label='Company')
    class Meta:
        model = User
'''
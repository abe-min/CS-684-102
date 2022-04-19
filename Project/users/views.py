from unicodedata import category
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
import requests
from newsapi import NewsApiClient
from .forms import RegisterForm, LoginForm, UpdateProfileForm
from rest_framework import viewsets
from .serializers import profileSerializer
from .models import Profile

user_key = ('General','Business','Entertainment','Health','Science','Sports','Technology')
#news api view
def home(request):
    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
    gen = newsapi.get_top_headlines(category='general')
    bus = newsapi.get_top_headlines(category='business')
    ent = newsapi.get_top_headlines(category='entertainment')
    health = newsapi.get_top_headlines(category='health')
    science = newsapi.get_top_headlines(category='science')
    tech = newsapi.get_top_headlines(category='technology')
    meh = []
    top =[]
    for field in user_key:
        #obj = Profile.objects.first()
        #field_object = Profile._meta.get_field(field)
        #field_value = field_object.value_from_object(obj)
        #if field_value is True:
        cat = "'" + field + "'"
        top = newsapi.get_top_headlines(category='general')
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    cat =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        #cat.append(f['category'])
    mylist = zip(news, desc, img)
    #mylist = zip(meh)
    return render(request, 'users/home.html', context ={"mylist":mylist})
    print (meh)


def homegen(request):
    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
    top = newsapi.get_top_headlines(category ='general')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    cat =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        #cat.append(f['category'])
    mylist = zip(news, desc, img)
    return render(request, 'users/home.html', context ={"mylist":mylist})

def homebus(request):
    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
    top = newsapi.get_top_headlines(category ='business')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    cat =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        #cat.append(f['category'])
    mylist = zip(news, desc, img)
    return render(request, 'users/home.html', context ={"mylist":mylist})


def homeent(request):
    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
    top = newsapi.get_top_headlines(category ='entertainment')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    cat =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        #cat.append(f['category'])
    mylist = zip(news, desc, img)
    return render(request, 'users/home.html', context ={"mylist":mylist})



def homehealth(request):
    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
    top = newsapi.get_top_headlines(category ='health')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    cat =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        #cat.append(f['category'])
    mylist = zip(news, desc, img)
    return render(request, 'users/home.html', context ={"mylist":mylist})



def homescience(request):
    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
    top = newsapi.get_top_headlines(category ='science')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    cat =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        #cat.append(f['category'])
    mylist = zip(news, desc, img)
    return render(request, 'users/home.html', context ={"mylist":mylist})



def homesport(request):
    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
    top = newsapi.get_top_headlines(category ='sports')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    cat =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        #cat.append(f['category'])
    mylist = zip(news, desc, img)
    return render(request, 'users/home.html', context ={"mylist":mylist})



def hometech(request):
    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
    top = newsapi.get_top_headlines(category ='technology')

    l = top['articles']
    desc =[]
    news =[]
    img =[]
    cat =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        #cat.append(f['category'])
    mylist = zip(news, desc, img)
    return render(request, 'users/home.html', context ={"mylist":mylist})


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
  
        if request.user.is_authenticated:
            return redirect(to='/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Remember me functionality 
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
    
            self.request.session.set_expiry(0)

      
            self.request.session.modified = True

     
        return super(CustomLoginView, self).form_valid(form)


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Settings have been saved successfully')
            return redirect(to='users-profile')

    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form})












#To be implemented in a later sprint

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')
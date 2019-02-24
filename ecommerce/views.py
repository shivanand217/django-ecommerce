# authentication
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ecommerce.forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title": "Home Page!!",
        "content": "Welcome to the Home page.",
    }
    # check authentication
    if request.user.is_authenticated():
        redirect("/login")
    else:
        return render(request,'home_page.html', context)

def about_page(request):
    context = {
        "title": "About Page!!",
        "content": "welcome to the About page..",
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    # django inbuilt form
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page!!",
        "content": "welcome to the Contact page..",
        "form": contact_form
    }
    if contact_form.is_valid():
        print("contact for has no errors", contact_form.cleaned_data)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print("fullname is %s" %(request.POST.get('fullname')))
    #     print("email is %s" %(request.POST.get('email')))
    #     print("content is %s" %(request.POST.get('content')))
    return render(request, "contact/view.html", context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("logging in user ", username)
            login(request, user)
            context['form'] = LoginForm() # reinitializes a new form
            # redirect to sucess page ...
            return redirect("/")
        else:
            # Return an 'invalid login' error message
            print("no such user exists...")
            pass
    return render(request, "auth/login.html", context)

def register_page(request):
    context = {}
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        print(register_form.cleaned_data)
    return render(request, "auth/register.html", context)

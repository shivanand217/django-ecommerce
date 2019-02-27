# authentication
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ecommerce.forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    home_page_context = {
        "title": "Home Page!!",
        "content": "Welcome to the Home page.",
    }
    # check authentication
    if request.user.is_authenticated():
        return render(request, 'home_page.html', home_page_context)
    else:
        return redirect('/login')

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
    print("Is User authenticated ?",request.user.is_authenticated())
    # if user is authenticated redirect him to home page
    if request.user.is_authenticated():
        print("user is",request.user)
        return redirect('/')
    if login_form.is_valid():
        print("login form cleaned data is:",login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print("user is ",user)
        if user is not None:
            login(request, user) # inbuilt login function
            context['form'] = LoginForm(request.POST or None) # reinitializes a new form
            return redirect('/')
        else:
            # Return an 'invalid login' error message
            print("no such user exists...")
            context['form'] = LoginForm() # reinitializes a new form
            return redirect('/login')
    return render(request, "auth/login.html", context)

def register_page(request):
    # check user authentication if user is already logged in then navigate him/her to the login page

    register_form = RegisterForm(request.POST or None)
    register_page_context = {
        "form": register_form
    }
    if register_form.is_valid():
        print("register form cleaned data is:",register_form.cleaned_data)
        firstname = register_form.cleaned_data.get("firstname")
        lastname = register_form.cleaned_data.get("lastname")
        email = register_form.cleaned_data.get("email")
        contact = register_form.cleaned_data.get("contact")
        # print("user name is %s %s", % (firstname,lastname))        
        register_page_context['form'] = RegisterForm(request.POST or None)

    return render(request, "auth/register.html", context)
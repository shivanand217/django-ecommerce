# for authentication
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ecommerce.forms import ContactForm, LoginForm, RegisterForm

# Function based views

# home view
def home_page(request):
    home_page_context = {
        "title": "Home Page!!",
        "content": "Welcome to the Home page."
    }
    # check authentication
    if request.user.is_authenticated():
        # show premium_content to the logined users
        home_page_context["premium_content"] = "YEAHHH"
        return render(request, 'home_page.html', home_page_context)
    else:
        return redirect('/login')

# about view
def about_page(request):
    context = {
        "title": "About Page!!",
        "content": "welcome to the About page..",
    }
    return render(request, "about_page.html", context)

# contact view
def contact_page(request):
    # django inbuilt form
    contact_form = ContactForm(request.POST or None)
    contact_page_context = {
        "title": "Contact Page!!",
        "content": "welcome to the Contact page..",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print("contact form has no errors", contact_form.cleaned_data)
    # check authentication
    if request.user.is_authenticated():
        return render(request, 'contact/view.html', contact_page_context)
    else:
        return redirect('/login')

# login view
def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    print("Is User authenticated?",request.user.is_authenticated())
    # if user is authenticated redirect to home page
    if request.user.is_authenticated():
        # print("user is",request.user)
        return redirect('/')
    if login_form.is_valid():
        print("login form cleaned data is:",login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
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

# logout view
def logout_page(request):
    if request.user.is_authenticated():
        print("user is",request.user)
        logout(request)
        return redirect('/login')
    else:
        return redirect('/login')

# get django built-in user_model
User = get_user_model()

# register page view
def register_page(request):
    # check user authentication if user is already logged in then navigate him/her to the login page if authenticated.
    register_form = RegisterForm(request.POST or None)
    register_page_context = {
        "form": register_form
    }
    # stuffs for form submission
    if register_form.is_valid():
        print("register form cleaned data is:",register_form.cleaned_data)
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        print(new_user)
        return redirect('/register')
    return render(request, 'auth/register.html', register_page_context)
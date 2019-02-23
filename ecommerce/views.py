from django.http import HttpResponse
from django.shortcuts import render

from ecommerce.forms import ContactForm

def home_page(request):
    context = {
        "title": "Home Page!!",
        "content": "Welcome to the Home page.",
    }
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

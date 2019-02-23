
from django.http import HttpResponse
from django.shortcuts import render

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
    context = {
        "title": "Contact Page!!",
        "content": "welcome to the Contact page.."
    }
    if request.method == "POST":
        #print(request.POST)
        print("fullname is %s" %(request.POST.get('fullname')))
        print("email is %s" %(request.POST.get('email')))
        print("content is %s" %(request.POST.get('content')))
    return render(request, "contact/view.html", context)

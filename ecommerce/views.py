from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title": "Home Page!!"
    }
    return render(request,'home_page.html', context)

def about_page(request):
    context = {
        "title": "About Page!!"
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    context = {
        "title": "Contact Page!!"
    }
    return render(request, "contact_page.html", context)

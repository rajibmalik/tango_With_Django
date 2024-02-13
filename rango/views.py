from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")

# Each view exists in views.py as series of individual functions. 
# Each view takes at least one arguement - a HttpRequest object, 
# (this lives in django.http module), convention dictates it is named 
# request
# Each view must return a HttpResponse object
# A simple HttpResponse object takes a string parameter 
# representing the content of the page we wish to send 
# to the client requesting the view

# For a user to see a view, we must map a Uniform Resource Locator(URL)
# to the view





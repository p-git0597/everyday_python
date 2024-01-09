from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    #handle the form here
    if request.method == "POST":
        name = (request.POST['name'])
        email = (request.POST['email'])
        phone = (request.POST['phone'])
        c = Contact(name = name, phone=phone, email=email)
        c.save
    return render(request, 'contact.html')
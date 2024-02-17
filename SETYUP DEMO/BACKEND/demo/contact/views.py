from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
# Create your views here.
def index(request):
    return render(request, 'contact/index.html')
def contactstored(request):
    if request.method=="POST":
        print(request)
        firstname=request.POST.get('firstname', '')
        lastname=request.POST.get('lastname', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('message', '')
        contact = Contact(contact_first_name=firstname, contact_last_name= lastname ,contact_email=email, contact_phone=phone, contact_desc=desc)
        contact.save()
    return redirect('index')

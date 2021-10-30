from django.core.checks import messages
from django.shortcuts import render
from shavi.models import Contact
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US </h1>")
    return render(request,'index.html')
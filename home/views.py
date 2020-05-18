from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    #return HttpResponse("This is about page")
    return render(request,'about.html')

def service(request):
    #return HttpResponse("This is service page")
    return render(request,'service.html')

def contact(request):
    #return HttpResponse("This is contact page")
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        contact=Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'Form has been submited')

    return render(request,'contact.html')

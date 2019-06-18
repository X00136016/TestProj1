from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request,*args,**kwargs):
    print(*args,**kwargs)
    print(request.user)
    return render(request, "home.html", {})

def phone_view(request, *args,**kwargs):
    print(*args,**kwargs)
    print(request.user)
    return render(request, "phones.html", {})
    
def contact_view(request, *args,**kwargs):
    return render(request, "contact.html", {})
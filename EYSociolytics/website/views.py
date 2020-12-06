from django.shortcuts import render
from django.views import View

# Create your views here.
def home(request):
    return render(request,"website/home.html")

def about(request):
    return render(request,"website/about.html")

def pricing(request):
    return render(request,"website/pricing.html")

def contact(request):
    return render(request,"website/contact.html")

def download(request):
    return render(request,"website/download.html")
    